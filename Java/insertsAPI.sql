-- 	Corrigir para proxima sprint, criar um banco separado para os dados internos;
INSERT INTO tbEmpresa VALUES(NULL,"92641676000182","Planeit","Planeit","Rua Haddock Lobo, 595");

INSERT INTO tbColaborador VALUES(NULL,"52813382000","Andrey Rodrigues","andrey.rodriges@gmail.com","12345678","Gerente",1,NULL,"69937584884",3,NULL),
								(NULL,"95906893024","Bruna Sanguini","bruna.sanguini@gmail.com","87654321","Analista de sistema",0,13,"83935572906",3,NULL),
                                (NULL,"11414310099","Caetano Resende","caetano.resente@gmail.com","12345678","Desenvolvedor web",0,13,"63925544693",3,NULL),
                                (NULL,"96501467098","Luanna Di Stefani","luanna.stefani@gmail.com","87654321","Desenvolvedt",0,13,"34922157817",3,NULL),
                                (NULL,"98219937025","Lucas Augusto","lucas.augusto@gmail.com","12345678","Analista de infraestrutura",1,13,"28926136281",3,NULL);

INSERT INTO tbAeroporto VALUES(NULL,"Planeit","Brasil","São Paulo","Rua Haddock Lobo",3);
INSERT INTO tbServidor VALUES(NULL,"ABC123","Servidor Interno","Red Het","4224513186","Servidor interno da empresa",19);


INSERT INTO tbUnidadeMedida VALUES (NULL,"Gigabyte","GB");
INSERT INTO tbUnidadeMedida VALUES (NULL," Megahertz","MHz");
INSERT INTO tbUnidadeMedida VALUES (NULL,"Porcentagem","%");
INSERT INTO tbUnidadeMedida VALUES (NULL,"Inteiro","");
INSERT INTO tbUnidadeMedida VALUES (NULL,"Graus Celsius","°C");
INSERT INTO tbUnidadeMedida VALUES(NULL,"Número de Processos","");

select * FROM tbColaborador;
Select * from tbEmpresa;
select * from tbServidor;