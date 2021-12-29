drop table if exists food;
drop table if exists week;
drop table if exists week_food;

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
