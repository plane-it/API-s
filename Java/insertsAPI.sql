SELECT * FROM tbEmpresa;
SELECT * FROM tbAeroporto;
SELECT * FROM tbColaborador;
SELECT * FROM tbServidor;
SELECT * FROM tbComponente;
SELECT * FROM tbTipoComponente;
SELECT * FROM tbUnidadeMedida;
SELECT * FROM tbMetrica;
select * FROM tbRegistro;
SELECT * FROM tbProcessos;

INSERT INTO tbEmpresa VALUES (null,'12345678900110', 'Azul Linhas Aéreas', 'Azul S.A.','');

INSERT INTO tbAeroporto VALUE(null,'Conconhas',"Brasil",'SP','',1);

-- INSERT INTO tbColaborador VALUES(null,'12345678901','teste','qwd','12345678','asd',false,null,"1234444",1,1);
INSERT INTO tbColaborador VALUES(null,'12345678902','teste','','','asd',false,null,"1234444",1,1);

INSERT INTO tbServidor VALUES(NULL,'123456','Servidor 1','Linux','123467','Sistema Aerio',1);

INSERT INTO tbTipoComponente VALUES(null,"CPU"),
								   (NULL,"RAM"),
                                   (NULL, "DISCO");

INSERT INTO tbComponente VALUES (NULL,"AMD",1,23.45,1),
								(NULL,"RAM",2,123.12,1),
                                (NULL,"Disco",3,122.12,1);
	

INSERT INTO tbUnidadeMedida VALUES (NULL,"Gigabyte","GB");
INSERT INTO tbUnidadeMedida VALUES (NULL," Megahertz","MHz");
INSERT INTO tbUnidadeMedida VALUES (NULL,"Porcentagem","%");
INSERT INTO tbUnidadeMedida VALUES (NULL,"Inteiro","");
INSERT INTO tbUnidadeMedida VALUES (NULL,"Graus Celsius","°C");
INSERT INTO tbUnidadeMedida VALUES(NULL,"Número de Processos","");

INSERT INTO tbMetrica VALUES(NULL,"2.80",1,2);
INSERT INTO tbMetrica VALUES(NULL,"50",1,3);
INSERT INTO tbMetrica VALUES(NULL,"70",1,5);
INSERT INTO tbMetrica VALUES(NULL,"500",null,6);