create table week (
  id integer primary key,
  exercise_id text,
  reps_5 text,
  reps_8 text,
  reps_13 text,
  reps_21 text
);

create table exercise (
  id text primary key,
  equipment_id text
);

create table equipment (
  id text primary key
);
