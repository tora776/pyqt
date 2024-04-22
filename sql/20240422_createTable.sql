CREATE TABLE account
(id SERIAL not null,
name text ,
address text,
tel char(13),
mail text,
add_date timestamp,
update_date timestamp,
delete_date timestamp,
PRIMARY KEY(id));