create table equipment (
    id text primary key
);

create table exercise (
  id text primary key,
  equipment_id text
);

create table week_exercise (
  week integer,
  exercise_id text,
  reps integer,
  resistance text,
  UNIQUE(week, exercise_id, reps)
);
