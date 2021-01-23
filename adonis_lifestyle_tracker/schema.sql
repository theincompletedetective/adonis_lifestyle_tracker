drop table if exists food;
drop table if exists week;
drop table if exists week_food;


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
    day_id text,
    food_id text
);
