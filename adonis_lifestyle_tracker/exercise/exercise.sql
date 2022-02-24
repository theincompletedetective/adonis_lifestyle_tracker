drop table if exists equipment;
drop table if exists exercise;


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
  reps13 text,
  reps15 text,
  reps21 text
);