drop table if exists Species;
create table Species (
  id integer primary key autoincrement,
  title text not null,
  text text not null
);