drop table if exists equipment;
drop table if exists exercise;
drop table if exists reps;
drop table if exists resistance;
drop table if exists day_of_week;
drop table if exists week_day;
drop table if exists week_exercise;


create table equipment (
    id text primary key
) WITHOUT ROWID;

create table exercise (
    id text primary key,
    equipment_id text
) WITHOUT ROWID;

create table reps (
    id integer primary key
) WITHOUT ROWID;

create table resistance (
    id text primary key
) WITHOUT ROWID;

create table day_of_week (
    id text primary key
) WITHOUT ROWID;

create table week_day (
    week_id integer,
    day_id text
) WITHOUT ROWID;

create table week_exercise (
    week_id integer,
    exercise_id integer,
    reps_id integer,
    resistance_id integer,
    UNIQUE(week_id, exercise_id, reps_id)
) WITHOUT ROWID;
