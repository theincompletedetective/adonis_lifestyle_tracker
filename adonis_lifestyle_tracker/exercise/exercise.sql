create table exercise (
  id text primary key,
  equipment text
);

create table week (
  id integer,
  exercise_id text,
  reps integer,
  resistance text
);