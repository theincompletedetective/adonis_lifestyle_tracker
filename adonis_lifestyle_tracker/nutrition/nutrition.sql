create table food (
    food text primary key,
    kcal integer,
    protein integer
);

create table week (
    id integer primary key,
    total_kcal integer,
    total_protein integer
);

create table food_week (
    food text,
    week integer
);
