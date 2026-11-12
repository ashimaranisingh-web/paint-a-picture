// Deletes the signed-in person's account: their sign-in, and with it their saved world.
// The app calls this from Account → Delete account. It only ever deletes the caller: the person is identified from
// their own sign-in token, never from anything sent in the request.
import { createClient } from "npm:@supabase/supabase-js@2.119.0";

const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
const reply = (status: number, body: Record<string, unknown>) =>
  new Response(JSON.stringify(body), { status, headers: { ...cors, "Content-Type": "application/json" } });

// The project's secret key. Supabase provides it to functions either in the new format (a JSON list of named secret
// keys) or the legacy one (the service_role key); take whichever is there.
function secretKey(): string {
  const raw = Deno.env.get("SUPABASE_SECRET_KEYS");
  if (raw) {
    try {
      const keys = JSON.parse(raw);
      if (typeof keys === "string") return keys;
      if (keys && typeof keys === "object") {
        const named = keys.default ?? Object.values(keys)[0];
        if (typeof named === "string" && named) return named;
      }
    } catch (_) {
      if (raw.startsWith("sb_secret_")) return raw; // a single key, not JSON
    }
  }
  return Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") ?? "";
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  if (req.method !== "POST") return reply(405, { error: "Use POST" });

  const token = (req.headers.get("Authorization") ?? "").replace(/^Bearer\s+/i, "");
  if (!token) return reply(401, { error: "Not signed in" });

  try {
    const url = Deno.env.get("SUPABASE_URL") ?? "", key = secretKey();
    if (!url || !key) return reply(500, { error: "The function can't reach its secret key", step: "config" });
    const admin = createClient(url, key, { auth: { persistSession: false, autoRefreshToken: false } });

    // who is asking: their token says, and only their own account can be deleted
    const { data: who, error: whoErr } = await admin.auth.getUser(token);
    if (whoErr || !who?.user) return reply(401, { error: "Not signed in" });
    const id = who.user.id;

    // Deleting the sign-in deletes their saved world with it (the worlds table cascades), in one step, so nothing is
    // ever left half-deleted. The row delete after it only tidies up if the cascade isn't there.
    const { error: userErr } = await admin.auth.admin.deleteUser(id);
    if (userErr) { console.error("deleteUser", userErr.message); return reply(500, { error: "Couldn't delete the sign-in", step: "user", detail: userErr.message }); }
    await admin.from("worlds").delete().eq("user_id", id);

    return reply(200, { deleted: true });
  } catch (e) {
    console.error("delete-account", e instanceof Error ? e.message : String(e));
    return reply(500, { error: "Something went wrong", step: "unexpected", detail: e instanceof Error ? e.message : String(e) });
  }
});
