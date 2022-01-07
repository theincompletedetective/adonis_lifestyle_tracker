drop table if exists food;
drop table if exists weekday;
drop table if exists week;
drop table if exists week_food;

create table food (
    id text primary key,
    calories real,
    protein real
);

create table weekday (
    week_id integer,
    sunday text,
    monday text,
    tuesday text,
    wednesday text,
    thursday text,
    friday text,
    saturday text
);

create table week (
    id integer primary key,
    total_calories real,
    total_protein real
);

create table week_food (
    week_id integer,
    weekday text,
    food_id text
);
