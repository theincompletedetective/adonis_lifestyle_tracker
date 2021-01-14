create table exercise (
  id text primary key,
  tool text
);

create table reps (
  id integer primary key
);

create table resistance (
  id text primary key
);

create table week (
  week_id integer,
  exercise_id text,
  reps_id integer,
  resistance_id text
);