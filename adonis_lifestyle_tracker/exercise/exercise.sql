create table week (
  id integer primary key
);

create table exercise (
  id text primary key,
  tool_id text
);

create table resistance (
  id text primary key
);

create table reps (
  id integer primary key
);


create table exercise_week (
  exercise_id text,
  week_id integer
);

create table exercise_reps_resistance (
  exercise_id text,
  reps_id integer,
  resistance_id text
);
