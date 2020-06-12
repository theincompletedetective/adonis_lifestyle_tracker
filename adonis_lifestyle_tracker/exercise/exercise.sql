create table exercise (
    id integer primary key,
    exercise_name text,
    equipment text,
    reps_5 text,
    reps_8 text,
    reps_13 text,
    reps_21 text
);

create table week (
    id integer primary key
);

create table exercise_week (
    exercise_id integer,
    week_id integer
);