create table week (
  id integer primary key
);

create table exercise (
  id text primary key
);

create table equipment (
  id text primary key
);

create table resistance (
  id text primary key
);

create table reps (
  id integer primary key
);

create table exercise_relation (
  week_id integer,
  exercise_id text,
  equipment_id text,
  resistance_id text,
  reps_id integer
);