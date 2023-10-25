
drop database if exists teste;
create database teste;
use teste;
create table teste(
	id int primary key auto_increment,
    siglaEmpresaAerea varchar(20),
    nVoo varchar(20),
    siglaAeroportoOrigem varchar(20),
    horaPartidaPrevista datetime,
    horaPartidaReal datetime,
    siglaAeroportoDestino varchar(30),
    horaChegadaPrevista datetime,
    horaChegadaReal datetime,
    situacao varchar(30)
);

drop procedure if exists deleteByMonth;
DROP TEMPORARY TABLE f exits TEMP;
DELIMITER $$
CREATE PROCEDURE deleteByMonth(deleteYear int,deleteMonth INT)
BEGIN 
    CREATE TEMPORARY TABLE temp
	SELECT id FROM teste
	WHERE
		(YEAR(horaPartidaPrevista) = deleteYear or YEAR(horaPartidaReal) = deleteYear) and
		(MONTH(horaPartidaPrevista) = deleteMonth OR MONTH(horaPartidaReal) = deleteMonth);

    DELETE FROM teste WHERE id IN (SELECT id FROM temp);

    DROP TEMPORARY TABLE temp;
END $$
