-- Paint a Picture: one world per person, readable and writable only by that person.
-- Run this once in your Supabase project: SQL Editor -> New query -> paste -> Run.

create table if not exists public.worlds (
  user_id    uuid primary key references auth.users (id) on delete cascade,
  data       jsonb not null,
  updated_at timestamptz not null default now()
);

alter table public.worlds enable row level security;

create policy "Read your own world"   on public.worlds for select using (auth.uid() = user_id);
create policy "Create your own world" on public.worlds for insert with check (auth.uid() = user_id);
create policy "Update your own world" on public.worlds for update using (auth.uid() = user_id) with check (auth.uid() = user_id);
create policy "Delete your own world" on public.worlds for delete using (auth.uid() = user_id);

-- Her name and email beside her world, so a row is easy to recognise in the Table Editor.
alter table public.worlds
  add column if not exists name  text,
  add column if not exists email text;
