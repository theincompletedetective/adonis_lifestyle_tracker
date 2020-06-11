create table food (
    id integer primary key,
    food_name text,
    brand text,
    kcal integer,
    protein integer
);

create table week (
    id integer primary key,
    total_kcal integer,
    total_protein integer
);

create table food_week (
    food_id integer,
    week_id integer
);