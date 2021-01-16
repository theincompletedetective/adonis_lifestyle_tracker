create table week (
  id integer primary key
);

create table equipment (
  id text primary key
);

create table exercise (
  id text primary key,
  equipment_id text
);

create table reps (
  id integer primary key
);

create table resistance (
  id text primary key
);

create table week_exercise (
  week_id integer,
  exercise_id text,
  reps_id integer,
  resistance_id text
);