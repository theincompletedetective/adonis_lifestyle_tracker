create table food (
    id integer primary key,
    food_name text,
    calories integer,
    protein integer
);

create table week (
    id integer primary key
);

create table food_week (
    food_id integer,
    week_id integer
);