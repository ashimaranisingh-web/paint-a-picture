// Deletes the signed-in person's account: their saved world first, then their sign-in.
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

// The secret key, from the new key system if it's there, otherwise the legacy service_role key.
function secretKey(): string {
  try {
    const keys = JSON.parse(Deno.env.get("SUPABASE_SECRET_KEYS") ?? "{}");
    if (keys.default) return keys.default;
  } catch (_) { /* fall through to the legacy key */ }
  return Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") ?? "";
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  if (req.method !== "POST") return reply(405, { error: "Use POST" });

  const token = (req.headers.get("Authorization") ?? "").replace(/^Bearer\s+/i, "");
  if (!token) return reply(401, { error: "Not signed in" });

  const admin = createClient(Deno.env.get("SUPABASE_URL") ?? "", secretKey(), { auth: { persistSession: false } });

  // who is asking: their token says, and only their own account can be deleted
  const { data: who, error: whoErr } = await admin.auth.getUser(token);
  if (whoErr || !who?.user) return reply(401, { error: "Not signed in" });
  const id = who.user.id;

  const { error: rowErr } = await admin.from("worlds").delete().eq("user_id", id);
  if (rowErr) return reply(500, { error: "Couldn't delete the saved world" });

  const { error: userErr } = await admin.auth.admin.deleteUser(id);
  if (userErr) return reply(500, { error: "Couldn't delete the sign-in" });

  return reply(200, { deleted: true });
});
