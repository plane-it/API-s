import conexao

def inserirFrequencia(frequenciaAtual,frequenciaLimite,idCpu,idServidor,fkMetrica,tempoChamado):
    aletar = frequenciaAtual > frequenciaLimite

    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s, %s, %s)"
    val = (frequenciaAtual,aletar,idServidor,idCpu,fkMetrica)

    envioBanco(sql,val)

    if(aletar and tempoChamado == 10):
        idRegistro = conexao.mycursor.lastrowid
        registrarChamado(idRegistro,frequenciaAtual,frequenciaLimite)
        

def inserirTemperatura(temperaturaAtual,temperaturaLimite,idCpu,idServidor,fkMetrica,tempoChamado):
    aletar = temperaturaAtual > temperaturaLimite

    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s, %s, %s)"
    val = (temperaturaAtual,aletar,idServidor,idCpu,fkMetrica)

    envioBanco(sql,val)

    if(aletar and tempoChamado == 10):
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



# def inserirBancoHD(dadoHDNumParcs,dadoHDTotal,dadoHDAtual,dadoHDPercent):

#     global ultimo_chamado_Disco

#     # sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
#     # val = (dadoHDNumParcs,3,1,1)

#     # conexao.mycursor.execute(sql, val)
#     # DB.commit()

#     # sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
#     # val = (dadoHDTotal,3,1,1)

#     # conexao.mycursor.execute(sql,val)
#     # DB.commit()

#     passou = int(dadoHDAtual > discoGbLimite);

#     sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s, %s, %s)"
#     val = (dadoHDAtual, passou, fkServidor, fkDisco, fkMetricaDiscoGbLimite)

#     try:
#         conexao.mycursor.execute(sql,val)
#         DB.commit()

#         id_inserido = conexao.mycursor.lastrowid

#         if passou == 1:
#             if datetime.now() - ultimo_chamado_Disco >= timedelta(minutes=10):

#                 if dadoHDAtual < float(discoGbLimite) * 1.1:
#                     prioridade = 'Baixo'
#                     tempo = '24 horas'
#                 elif dadoHDAtual < float(discoGbLimite) * 1.2:
#                     prioridade = 'Médio'
#                     tempo = '8 horas'
#                 else:
#                     prioridade = 'Alto'
#                     tempo = '4 horas'

#                 sql = "INSERT INTO tbChamados VALUES (null, %s, %s, 'Aberto', %s)"
#                 val = (prioridade, tempo, id_inserido)
#                 conexao.mycursor.execute(sql,val)
#                 DB.commit()

#                 ultimo_chamado_Disco = datetime.now()


#     except Exception as e:
#         print("Ocorreu um erro no disco:", e)


#     # sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
#     # val = (dadoHDPercent,3,1,1)

#     # conexao.mycursor.execute(sql,val)
#     # DB.commit()

# def inserirBancoRam(dadoRAMTotal,dadoRAMAtual,dadoRAMPercent):

#     global ultimo_chamado_Ram

#     # sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
#     # val = (dadoRAMTotal,2,1,1)

#     # conexao.mycursor.execute(sql, val)
#     # DB.commit()

#     passou = int(dadoRAMAtual > ramGbLimite)

#     sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s, %s, %s)"
#     val = (dadoRAMAtual, passou, fkServidor, fkRam, fkMetricaRamGbLimite)

#     try:
#         conexao.mycursor.execute(sql,val)
#         DB.commit()

#         id_inserido = conexao.mycursor.lastrowid

#         if passou == 1:
#             if datetime.now() - ultimo_chamado_Ram >= timedelta(minutes=10):

#                 if dadoRAMAtual < float(ramGbLimite) * 1.1:
#                     prioridade = 'Baixo'
#                     tempo = '24 horas'
#                 elif dadoRAMAtual < float(ramGbLimite) * 1.2:
#                     prioridade = 'Médio'
#                     tempo = '8 horas'
#                 else:
#                     prioridade = 'Alto'
#                     tempo = '4 horas'

#                 sql = "INSERT INTO tbChamados VALUES (null, %s, %s, 'Aberto', %s)"
#                 val = (prioridade, tempo, id_inserido)
#                 conexao.mycursor.execute(sql,val)
#                 DB.commit()

#     except Exception as e:
#         print("Ocorreu um erro na ram:", e)


#     # sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
#     # val = (dadoRAMPercent,2,1,1)

#     # conexao.mycursor.execute(sql,val)
#     # DB.commit()

def envioBanco(sql,val):
    conexao.mycursor.execute(sql,val)
    conexao.DB.commit()