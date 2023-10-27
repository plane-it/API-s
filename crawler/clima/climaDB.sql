create database climaDados;
use climaDados;
drop table tbClima;
create table tbClima(
id int primary key auto_increment,
regiao char(2),
dataCompleta date,
hora time,
precipitacaoTotal double,
pressaoAtm double,
temperaturaAr double,
temperaturaOrv double,
temperaturaMax double,
temperaturaMin double,
umidadeRelativa int,
velocidadeAr double
);
select * from tbClima;
 