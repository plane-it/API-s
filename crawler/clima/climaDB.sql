drop database if exists climadados;
create database climaDados;

use climaDados;
drop table if exists tbSudeste; 
drop table if exists tbSul; 
drop table if exists tbCentroOeste; 
drop table if exists tbNordeste; 
drop table if exists tbNorte; 
-- Tabelas de cada região do Brasil
create table tbSudeste(
id int primary key auto_increment,
localizacao varchar(255),
regiao char(2),
dataCompleta date,
hora longtext,
precipitacao double
-- temperaturaAr double,
-- temperaturaOrv double,
-- temperaturaMax double,
-- temperaturaMin double,
-- umidadeRelativa int,
-- velocidadeAr double
);

create table tbSul(
id int primary key auto_increment,
localizacao varchar(255),
regiao char(2),
dataCompleta date,
hora longtext,
precipitacao double
-- temperaturaAr double,
-- temperaturaOrv double,
-- temperaturaMax double,
-- temperaturaMin double,
-- umidadeRelativa int,
-- velocidadeAr double
);

create table tbCentroOeste(
id int primary key auto_increment,
localizacao varchar(255),
regiao char(2),
dataCompleta date,
precipitacao double
-- temperaturaAr double,
-- temperaturaOrv double,
-- temperaturaMax double,
-- temperaturaMin double,
-- umidadeRelativa int,
-- velocidadeAr double
);

create table tbNordeste(
id int primary key auto_increment,
localizacao varchar(255),
regiao char(2),
dataCompleta date,
hora longtext,
precipitacao double
-- temperaturaAr double,
-- temperaturaOrv double,
-- temperaturaMax double,
-- temperaturaMin double,
-- umidadeRelativa int,
-- velocidadeAr double
);

create table tbNorte(
id int primary key auto_increment,
localizacao varchar(255),
regiao char(2),
dataCompleta date,
hora longtext,
precipitacao double
-- temperaturaAr double,
-- temperaturaOrv double,
-- temperaturaMax double,
-- temperaturaMin double,
-- umidadeRelativa int,
-- velocidadeAr double
);

SELECT * FROM tbSudeste ORDER BY id DESC;
SELECT * FROM tbSul ORDER BY id DESC;
SELECT * FROM tbCentroOeste ORDER BY id DESC;
SELECT * FROM tbNordeste ORDER BY id DESC;
SELECT * FROM tbNorte ORDER BY id DESC;