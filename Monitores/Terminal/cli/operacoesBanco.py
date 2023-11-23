import conexao
from decimal import Decimal


def inserirFrequencia(frequenciaAtual,frequenciaLimite,idCpu,idServidor,fkMetrica,tempoChamado):
    aletar = frequenciaAtual > frequenciaLimite

    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s, %s, %s)"
    val = (frequenciaAtual,aletar,idServidor,idCpu,fkMetrica)

    envioBanco(sql,val)

    if(aletar and tempoChamado == 10):
        idRegistro = conexao.mycursor.lastrowid
        registrarChamado(idRegistro,frequenciaAtual,frequenciaLimite)
        

def inserirTemperatura(temperaturaAtual,temperaturaLimite,idCpu,idServidor,fkMetrica,tempoChamado):
    temperaturaAtual = Decimal(temperaturaAtual['coretemp'][0].current)    
    alerta = temperaturaAtual > temperaturaLimite

    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s, %s, %s)"
    val = (temperaturaAtual, alerta, idServidor, idCpu, fkMetrica)

    envioBanco(sql,val)

    if(alerta and tempoChamado == 10):
        idRegistro = conexao.mycursor.lastrowid
        registrarChamado(idRegistro,temperaturaAtual,temperaturaLimite)

def inseritPorcentagemCpu(porcentagemAtual,porcentagemLimite,idCpu,idServidor,fkMetrica,tempoChamado):
    aletar = porcentagemAtual > porcentagemLimite

    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s, %s, %s)"
    val = (porcentagemAtual,aletar,idServidor,idCpu,fkMetrica)

    envioBanco(sql,val)

    if(aletar and tempoChamado == 10):
        idRegistro = conexao.mycursor.lastrowid
        registrarChamado(idRegistro,porcentagemAtual,porcentagemLimite)

def inseritPorcentagemCpu(porcentagemAtual,porcentagemLimite,idCpu,idServidor,fkMetrica,tempoChamado):
    aletar = porcentagemAtual > porcentagemLimite

    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s, %s, %s)"
    val = (porcentagemAtual,aletar,idServidor,idCpu,fkMetrica)

    envioBanco(sql,val)

    if(aletar and tempoChamado == 10):
        idRegistro = conexao.mycursor.lastrowid
        registrarChamado(idRegistro,porcentagemAtual,porcentagemLimite)

def inserirHdAtual(usoAtual,usoLimite,idCpu,idServidor,fkMetrica,tempoChamado):
    aletar = usoAtual > usoLimite

    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s, %s, %s)"
    val = (usoAtual,aletar,idServidor,idCpu,fkMetrica)

    envioBanco(sql,val)

    if(aletar and tempoChamado == 10):
        idRegistro = conexao.mycursor.lastrowid
        registrarChamado(idRegistro,usoAtual,usoLimite)


def inserirRamAtual(usoAtual,usoLimite,idCpu,idServidor,fkMetrica,tempoChamado):
    aletar = usoAtual > usoLimite

    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s, %s, %s)"
    val = (usoAtual,aletar,idServidor,idCpu,fkMetrica)

    envioBanco(sql,val)

    if(aletar and tempoChamado == 10):
        idRegistro = conexao.mycursor.lastrowid
        registrarChamado(idRegistro,usoAtual,usoLimite)


def registrarChamado(idRegistro,valorAtual,valorLimite):

    if(valorAtual <= (float(valorLimite) * 1.3)):
        sql = "INSERT INTO tbChamados VALUES (null,'Baixa','24 horas','Aberto',%s);"

    elif(valorAtual <= (float(valorLimite) * 1.6)):
        sql = "INSERT INTO tbChamados VALUES (null,'Média','8 horas','Aberto',%s);"

    else:
        sql = "INSERT INTO tbChamados VALUES (null,'Alta','4 horas','Aberto',%s);"


    envioBanco(sql,[(idRegistro)])


def envioBanco(sql,val):
    conexao.mycursor.execute(sql,val)
    conexao.DB.commit()