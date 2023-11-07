import usuario
import servidor
import coresTerminal as cores
import metricas

import psutil as ps
from pick import pick
import os
import time as t
import keyboard as k
from dotenv import load_dotenv
from getpass import getpass
from decimal import Decimal
from datetime import datetime, timedelta
import platform

# ================================================================= Carregando variaveis de ambiente
load_dotenv()

isRunning = False

# cpuFreqLimite = 0.0
# cpuTempLimite = 0.0
# ramGbLimite = 0.0
# discoGbLimite = 0.0

# fkMetricaCpuFreqLimite = 0
# fkMetricaCpuTempLimite = 0
# fkMetricaRamGbLimite = 0
# fkMetricaDiscoGbLimite = 0

# ultimo_chamado_CPU_Freq = datetime.now() - timedelta(minutes=10)
# ultimo_chamado_CPU_Temp = datetime.now() - timedelta(minutes=10)
# ultimo_chamado_Ram = datetime.now() - timedelta(minutes=10)
# ultimo_chamado_Disco = datetime.now() - timedelta(minutes=10)

# ================================================================= Login do usuário
def loginUsuario():

    user = usuario.Usuario(
        input("Digite o email de usuário: "),
        getpass("Digite a sua senha: ")
    )

    resultadoColaborador = usuario.autenticacao(user.usuario,user.senha)

    if len(resultadoColaborador) > 0:
        
        print(cores.verde + "\nSeja bem vindo(a): " + cores.fechamento  + resultadoColaborador[0][2] + "\n")
        
        fkEmpresa = resultadoColaborador[0][-2]
        loginServidor(fkEmpresa)

    else:
        print("\n" + cores.vermelho + "Houve um erro na autenticação do usuario, tente novamente" + cores.fechamento) 
        loginUsuario()

# ================================================================= Login servidor
def loginServidor(fkEmpresa):

    codigoAutenticacaoServidor = input("Digite o código do servidor: ")
    resultadoServidore = servidor.autenticar(fkEmpresa,codigoAutenticacaoServidor)

    if len(resultadoServidore) > 0:
        
        print(cores.verde + "Servidor autenticado" + cores.fechamento + "\n")
        buscarComponentesServidor(resultadoServidore[0][0])

    else:
        print("\n" + cores.vermelho + "Houve um erro na autenticação do servidor, tente novamente" + cores.fechamento + "\n") 
        loginServidor(fkEmpresa)


# ================================================================= Login servidor
def buscarComponentesServidor(fkServidor):
    
    print(cores.azul + "Buscando componentes..." + cores.fechamento)

    resultadoComponentes = servidor.buscarComponetes(fkServidor)

    for resultado in resultadoComponentes:
        idCompontente = resultado[0]
        tipoComponente = resultado[1]

        if (tipoComponente == 1) :
            global idCpu
            idCpu = idCompontente

        if (tipoComponente == 2) :
            global idRam
            idRam = idCompontente
    
        if (tipoComponente == 3) :
           global idDisco
           idDisco = idCompontente

    if (idCpu is not None or idRam is not None or idDisco is not None) :
        print(cores.azul + "Componentes encontrados!" + cores.fechamento)
        buscarMetricas()
    
    else:
        print(cores.vermelho + "Houve um erro na procura de componentes, tentaremos novamente"  + cores.fechamento)
        buscarComponentesServidor(fkServidor)


def buscarMetricas():

    print(cores.azul + "buscando metricas!" + cores.fechamento + "\n")

    metricasCPU = metricas.metricas(idCpu)
    metricasRam = metricas.metricas(idRam)
    metricasDisco = metricas.metricas(idDisco)

    print(metricasCPU)
    print(metricasRam)
    print(metricasDisco)



#                           CPU                        CPU                  
#   for resultado in metricasCPU :
#                         if (resultado[1] == 1) :
#                             cpuTempLimite = resultado[0]
#                             fkMetricaCpuTe
# 
# mpLimite = resultado[2]
#                             print(fkMetricaCpuTempLimite)
                            
#                             cpuTempLimite = Decimal(cpuTempLimite) * Decimal('0.8')
#                         else :
#                             cpuFreqLimite = resultado[0]
#                             fkMetricaCpuFreqLimite = resultado[2]
#                             print(fkMetricaCpuFreqLimite)
#                             print('e freq')
#                             cpuFreqLimite = cpuFreqLimite*0.8
                
                    
#           RAM                        RAM                         RAM                   RAM                  
#   ramGbLimite = metricasRam[0][0]
#                     fkMetricaRamGbLimite = metricasRam[0][1]
                    
#                     ramGbLimite = Decimal(ramGbLimite) * Decimal('0.8')
                

#   DISCO                 DISCO                      DISCO                      DISCO               
#   
                
#                     discoGbLimite = metricasDisco[0][0]
#                     fkMetricaDiscoGbLimite = metricasDisco[0][1]
                                        
#                     discoGbLimite = Decimal(discoGbLimite) * Decimal('0.8')
                    
#             print("Seja bem-vindo!")        
#             isRunning = True        
#             break       
                              
# # ================================================================= Funções de inserção no banco 
# def inserirBancoCPU(dadoCPUFisc,dadoCPULogc,dadoCPUFreq,dadoCPUPercent):
    
#     global ultimo_chamado_CPU_Temp
#     global ultimo_chamado_CPU_Freq
    
#     # sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
#     # val = (dadoCPUFisc,1,1,1)

#     # conexao.mycursor.execute(sql, val)
#     # DB.commit()
    
#     # sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
#     # val = (dadoCPULogc,1,1,1)
 
#     # conexao.mycursor.execute(sql,val)
#     # DB.commit()
    
#     passou = int(dadoCPUFreq > cpuFreqLimite)

#     sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s, %s, %s)"
#     val = (dadoCPUFreq, passou, fkServidor, fkCpu, fkMetricaCpuFreqLimite)

#     if fkMetricaCpuFreqLimite != 0:
#         try:
#             conexao.mycursor.execute(sql,val)
#             DB.commit()

#             id_inserido = conexao.mycursor.lastrowid

#             if passou == 1:
#                 if datetime.now() - ultimo_chamado_CPU_Freq >= timedelta(minutes=10):
                    
#                     prioridade = None
                    
#                     if dadoCPUFreq < float(cpuFreqLimite) * 1.1:
#                         prioridade = 'Baixo'
#                         tempo = '24 horas'
#                     elif dadoCPUFreq < float(cpuFreqLimite) * 1.2:
#                         prioridade = 'Médio'
#                         tempo = '8 horas'
#                     else:
#                         prioridade = 'Alto'
#                         tempo = '4 horas'

#                     sql = "INSERT INTO tbChamados VALUES (null, %s, %s, 'Aberto', %s)"
#                     val = (prioridade, tempo, id_inserido)
#                     conexao.mycursor.execute(sql,val)
#                     DB.commit()
                    
#                     ultimo_chamado_CPU_Freq = datetime.now()

#         except Exception as e:
#             print("Ocorreu um erro na cpu Freq:", e)


  
#     # sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
#     # val = (dadoCPUPercent,1,1,1)

#     # conexao.mycursor.execute(sql,val)
#     # DB.commit() 

#     if(platform.uname().system != 'Windows'):

#         dadoCPUTemp = ps.sensors_temperatures(fahrenheit=False)
#         dadoCPUTemp = list(dadoCPUTemp.values())[0][0].current       


#         passou = int(dadoCPUTemp > cpuTempLimite)

#         sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s, %s, %s)"
#         val = (dadoCPUTemp, passou, fkServidor, fkCpu, fkMetricaCpuTempLimite)

#         if fkMetricaCpuTempLimite != 0:
#             try:
#                 conexao.mycursor.execute(sql,val)
#                 DB.commit()

#                 id_inserido = conexao.mycursor.lastrowid

#                 if passou == 1:
#                     if datetime.now() - ultimo_chamado_CPU_Temp >= timedelta(minutes=10):

#                         if dadoCPUTemp < float(cpuTempLimite) * 1.1:
#                             prioridade = 'Baixo'
#                             tempo = '24 horas'
#                         elif dadoCPUTemp < float(cpuTempLimite) * 1.2:
#                             prioridade = 'Médio'
#                             tempo = '8 horas'
#                         else:
#                             prioridade = 'Alto'
#                             tempo = '4 horas'

#                         sql = "INSERT INTO tbChamados VALUES (null, %s, %s, 'Aberto', %s)"
#                         val = (prioridade, tempo, id_inserido)
#                         conexao.mycursor.execute(sql,val)
#                         DB.commit()
                        
#                         ultimo_chamado_CPU_Temp = datetime.now()


#             except Exception as e:
#                 print("Ocorreu um erro na cpu temp:", e)


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
  

# # ================================================================= Configurações do programa
# while isRunning:
#     opcoesInicio = ['Verificar Dados', 'Configurações', 'Sair']

#     opcEscolhida, index = pick(opcoesInicio, indicator='=>', default_index=0)


# # ================================================================= Captura de Dados 

#     if(opcEscolhida == 'Verificar Dados'):
#         while True:
#             dadoCPUFisc = ps.cpu_count(False) if user.CPUFisc else None
#             dadoCPULogc = ps.cpu_count(True) if user.CPULogc else None
#             dadoCPUFreq = round(ps.cpu_freq(False).current, 2) if user.CPUFreq else None
#             dadoCPUPercent = round(ps.cpu_percent(), 2) if user.CPUPercent else None

#             disks = ps.disk_partitions()
#             dadoHDNumParcs = len(disks) if user.HDNumParcs else None
#             dadoHDTotal = round((ps.disk_usage("/").total)*10**-9,2) if user.HDTotal else None
#             dadoHDAtual = round((ps.disk_usage("/").used)*10**-9,2) if user.HDAtual else None
#             dadoHDPercent = ps.disk_usage("/").percent if user.HDPercent else None

#             dadoRAMTotal = round((ps.virtual_memory().total)*10**-9,2) if user.RAMTot else None
#             dadoRAMAtual = round((ps.virtual_memory().used)*10**-9,2) if user.RAMAtual else None
#             dadoRAMPercent = ps.virtual_memory().percent if user.RAMPercent else None
            
#             os.system('cls' if os.name == 'nt' else 'clear')
#             print(f"""
#                                     CPU
#     ===========================================================================
#             | Processadores físicos: {dadoCPUFisc}
#             | Processadores Lógicos: {dadoCPULogc}
#             | Frequência da CPU: {dadoCPUFreq}MHz
#             | Porcentagem de uso da CPU: {dadoCPUPercent} %
#     ===========================================================================
                
#                                     ARMAZENAMENTO
#     ===========================================================================
#             | Partições: {dadoHDNumParcs}
#             | Armazenamento total: {dadoHDTotal} GB
#             | Uso atual: {dadoHDAtual} GB
#             | Porcentagem de uso: {dadoHDPercent} %
#     ===========================================================================
                
#                                     MEMÓRIA
#     ===========================================================================
#             | Quantidade total de RAM: {dadoRAMTotal} GB
#             | Uso atua de RAM: {dadoRAMAtual} GB
#             | Porcentagem de uso: {dadoRAMPercent} %
#     ===========================================================================

#     (Pressione [ESC] para voltar)
#                 """)
    
#             inserirBancoCPU(dadoCPUFisc,dadoCPULogc,dadoCPUFreq,dadoCPUPercent)
#             inserirBancoHD(dadoHDNumParcs,dadoHDTotal,dadoHDAtual,dadoHDPercent)
#             inserirBancoRam(dadoRAMTotal,dadoRAMAtual,dadoRAMPercent)
    
#             if k.read_key() == 'esc':
#                 break

#             t.sleep(1)

    
# # ================================================================= Configurações

#     elif (opcEscolhida == 'Configurações'):
#         opcoesConfig = ['CPU', 'HD', 'RAM', "Voltar"]
#         opcHardware, index = pick(opcoesConfig, indicator='=>', default_index=0)
#         opcEscolha = ['True', 'False']

# # ================================================================= CPU
    
#         if (opcHardware == 'CPU'):
#             opcoesCPU = ['Processadores físicos', 'Processadores Lógicos', 'Frequência de CPU', 'Porcentagem de uso da CPU', 'Voltar']
#             opcConfigCPU, index = pick(opcoesCPU, indicator='=>', default_index=0)
        
#             if(opcConfigCPU == 'Processadores físicos'):
#                 opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                
#                 if(opcEscolha == 'True'): 
#                     user.CPUFisc = True
#                 else: user.CPUFisc = False
            
#             elif(opcConfigCPU == 'Processadores Lógicos'):
#                 opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                            
#                 if(opcEscolha == 'True'): 
#                     user.CPULogc = True
#                 else: user.CPULogc = False

#             elif(opcConfigCPU == 'Frequência de CPU'):
#                 opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                            
#                 if(opcEscolha == 'True'): 
#                     user.CPUFreq = True
#                 else: user.CPUFreq = False  

#             elif(opcConfigCPU == 'Porcentagem de uso da CPU'):
#                 opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                            
#                 if(opcEscolha == 'True'): 
#                     user.CPUPercent = True
#                 else: user.CPUPercent = False            

# # ================================================================= HD

#         elif(opcHardware == 'HD'):
#             opcoesHD = ['Partições do HD', 'Armazenamento total', 'Armazenamento atual', 'Porcentagem de uso do HD', 'Voltar']
#             opcConfigHD, index = pick(opcoesHD, indicator='=>', default_index=0)
            
#             if(opcConfigHD == 'Partições do HD'):
#                 opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                
#                 if(opcEscolha == 'True'): 
#                     user.HDNumParcs = True
#                 else: user.HDNumParcs = False

#             elif(opcConfigHD == 'Armazenamento total'):
#                 opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                
#                 if(opcEscolha == 'True'): 
#                     user.HDTotal = True
#                 else: user.HDTotal = False

#             elif(opcConfigHD == 'Armazenamento atual'):
#                 opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                
#                 if(opcEscolha == 'True'): 
#                     user.HDAtual = True
#                 else: user.HDAtual = False
                
#             elif(opcConfigHD == 'Porcentagem de uso do HD'):
#                 opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                
#                 if(opcEscolha == 'True'): 
#                     user.HDPercent = True
#                 else: user.HDPercent = False

# #======================================================================================== RAM
#         elif(opcHardware == 'RAM'):
#             opcoesRAM = ['Quantidade total de RAM', 'Uso atual de RAM', 'Porcentagem de uso da RAM', 'Voltar']
#             opcConfingRAM, index = pick(opcoesRAM, indicator='=>', default_index=0)
            
#             if(opcConfingRAM == 'Partições do HD'):
#                 opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                
#                 if(opcEscolha == 'True'): 
#                     user.RAMTot = True
#                 else: user.RAMTot = False

#             elif(opcConfingRAM == 'Uso atual de RAM'):
#                 opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                
#                 if(opcEscolha == 'True'): 
#                     user.RAMAtual = True
#                 else: user.RAMAtual = False

#             elif(opcConfingRAM == 'Porcentagem de uso da RAM'):
#                 opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                
#                 if(opcEscolha == 'True'): 
#                     user.RAMPercent = True
#                 else: user.RAMPercent = False


# #====================================================================================== Sair

#     elif(opcEscolhida == 'Sair'):
#         break


loginUsuario()