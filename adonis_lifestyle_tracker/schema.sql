drop table if exists food;
drop table if exists week;
drop table if exists week_food;
drop table if exists equipment;
drop table if exists exercise;
drop table if exists week_exercise;


-- Nutrition Tables
create table food (
    id text primary key,
    calories integer,
    protein integer
);

create table week (
    id integer primary key,
    total_calories integer,
    total_protein integer
);

create table week_food (
    week_id integer,
    food_id text
);


--Exercise Tables
create table equipment (
    id text primary key
);

create table exercise (
  id text primary key,
  equipment_id text,
  reps3 text,
  reps5 text,
  reps6 text,
  reps7 text,
  reps8 text,
  reps10 text,
  reps12 text,
  reps15 text,
  reps13 text,
  reps21 text
);

create table week_exercise (
  week integer,
  exercise_id text,
  UNIQUE(week, exercise_id)
);
