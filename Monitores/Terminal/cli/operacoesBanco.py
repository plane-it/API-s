import conexao
import slack
import jira
from decimal import Decimal


def inserirFrequencia(frequenciaAtual,frequenciaLimite,idCpu,idServidor,fkMetrica,tempoChamado):
    unidadeMedida = "MHz"
    tipoComponente = "CPU"

    aletar = frequenciaAtual > frequenciaLimite

    print(aletar)

    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s, %s, %s)"
    val = (frequenciaAtual,aletar,idServidor,idCpu,fkMetrica)

    envioBanco(sql,val)

    if(aletar and tempoChamado == 10):
        idRegistro = conexao.mycursor.lastrowid
        registrarChamado(idRegistro, frequenciaAtual, frequenciaLimite, idCpu, idServidor, tipoComponente, unidadeMedida)
        

def inserirTemperatura(temperaturaAtual,temperaturaLimite,idCpu,idServidor,fkMetrica,tempoChamado):
    unidadeMedida = "°C"
    tipoComponente = "CPU"

    temperaturaAtual = Decimal(temperaturaAtual['coretemp'][0].current)    
    alerta = temperaturaAtual > temperaturaLimite

    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s, %s, %s)"
    val = (temperaturaAtual, alerta, idServidor, idCpu, fkMetrica)

    envioBanco(sql,val)

    if(alerta and tempoChamado == 10):
        idRegistro = conexao.mycursor.lastrowid
        registrarChamado(idRegistro, temperaturaAtual, temperaturaLimite, idCpu, idServidor, tipoComponente, unidadeMedida)

def inseritPorcentagemCpu(porcentagemAtual,porcentagemLimite,idCpu,idServidor,fkMetrica,tempoChamado):
    unidadeMedida = "%"
    tipoComponente = "CPU"

    aletar = porcentagemAtual > porcentagemLimite

    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s, %s, %s)"
    val = (porcentagemAtual,aletar,idServidor,idCpu,fkMetrica)

    envioBanco(sql,val)

    if(aletar and tempoChamado == 10):
        idRegistro = conexao.mycursor.lastrowid
        registrarChamado(idRegistro, porcentagemAtual, porcentagemLimite, idCpu, idServidor, tipoComponente, unidadeMedida)

def inserirHdAtual(usoAtual,usoLimite,idDisco,idServidor,fkMetrica,tempoChamado):
    unidadeMedida = "Gb"
    tipoComponente = "Disco"
    
    aletar = usoAtual > usoLimite

    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s, %s, %s)"
    val = (usoAtual,aletar,idServidor,idDisco,fkMetrica)

    envioBanco(sql,val)

    if(aletar and tempoChamado == 10):
        idRegistro = conexao.mycursor.lastrowid
        registrarChamado(idRegistro, usoAtual, usoLimite, idDisco, idServidor, tipoComponente, unidadeMedida)


def inserirRamAtual(usoAtual,usoLimite,idRam,idServidor,fkMetrica,tempoChamado):
    unidadeMedida = "Gb"
    tipoComponente = "RAM"

    aletar = usoAtual > usoLimite

    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s, %s, %s)"
    val = (usoAtual,aletar,idServidor,idRam,fkMetrica)

    envioBanco(sql,val)

    if(aletar and tempoChamado == 10):
        idRegistro = conexao.mycursor.lastrowid
        registrarChamado(idRegistro, usoAtual, usoLimite, idRam, idServidor, tipoComponente, unidadeMedida)


def registrarChamado(idRegistro, valorAtual, valorLimite, idComponente, idServidor, tipoComponente, unidadeMedida):

    if(valorAtual <= (float(valorLimite) * 1.3)):
        mensagem = slack.montarMensagem(idComponente, tipoComponente, idServidor, valorLimite, unidadeMedida, valorAtual, 'Baixa')
        sql = "INSERT INTO tbChamados VALUES (null,'Baixa','24 horas','Aberto',%s);"

    elif(valorAtual <= (float(valorLimite) * 1.6)):
        mensagem = slack.montarMensagem(idComponente, tipoComponente, idServidor, valorLimite, unidadeMedida, valorAtual, 'Media')
        sql = "INSERT INTO tbChamados VALUES (null,'Média','8 horas','Aberto',%s);"

    else:
        mensagem = slack.montarMensagem(idComponente, tipoComponente, idServidor, valorLimite, unidadeMedida, valorAtual, 'Alta')
        sql = "INSERT INTO tbChamados VALUES (null,'Alta','4 horas','Aberto',%s);"

    slack.enviarMensagem(mensagem)
    jira.criarChamadoJira(mensagem)
    envioBanco(sql,[(idRegistro)])

def registrarSpec(valor, idComponente, idUnidadeMedida) :
    sql = "INSERT INTO tbSpecs VALUES (NULL, %s, %s, %s)"
    val = [valor, idComponente, idUnidadeMedida]

    envioBanco(sql,val)

def envioBanco(sql,val):
    conexao.mycursor.execute(sql,val)
    conexao.DB.commit()