create database banquinho;

use banquinho;

create table mesa(
id int auto_increment not null primary key,
Cidade varchar(50) not null,
Temperatura varchar(10) not null,
Descricao varchar(65) not null,
Data_atual varchar(12) not null,
Speed varchar(4) not null,
Clouds varchar(20) not null,
Humidity varchar(40) not null
);

