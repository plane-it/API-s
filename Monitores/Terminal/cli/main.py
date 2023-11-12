import usuario
import servidor
import coresTerminal as cores
import operacoesBanco 

import psutil as ps
from pick import pick
import os
import time as t
import keyboard as k
from dotenv import load_dotenv
from getpass import getpass
import platform

# ================================================================= Carregando variaveis de ambiente
load_dotenv()

tempoChamado = 1

# ================================================================= Login do usuário
def loginUsuario():
    global user
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
    resultadoServidor = servidor.autenticar(fkEmpresa,codigoAutenticacaoServidor)

    if len(resultadoServidor) > 0:

        print(cores.verde + "Servidor autenticado" + cores.fechamento + "\n")

        global idServidor
        idServidor = resultadoServidor[0][0]
        buscarComponentesServidor(idServidor)

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

# ================================================================= Buscar Metrica
def buscarMetricas():

    print(cores.azul + "buscando metricas!" + cores.fechamento)

    metricasCPU = servidor.metricas(idCpu)
    metricasRam = servidor.metricas(idRam)
    metricasDisco = servidor.metricas(idDisco)

    criacaoVariaveisMetricaCPU(metricasCPU)
    criacaoVariaveisMetricaRam(metricasRam)
    criacaoVariaveisMetricaDisco(metricasDisco)

    print(cores.azul + "busca de metricas concluida!" + cores.fechamento + "\n")

    opcoesMenu()


# ================================================================= Criação das variaveis das metricas
def criacaoVariaveisMetricaCPU(metricas):

    for resultado in metricas:
        if(resultado[1] == 1):
            global limiteTemperaturaCpu
            limiteTemperaturaCpu = resultado[0]

            global fkMetricaLimiteTemperaturaCpu
            fkMetricaLimiteTemperaturaCpu = resultado[2]

        elif (resultado[1] == 2):

            global limiteUsoCpu
            limiteUsoCpu = resultado[0]

            global fkMetricaLimiteUsoCpu
            fkMetricaLimiteUsoCpu = resultado[2]

        else:

            global limiteFrequenciaCpu
            limiteFrequenciaCpu = resultado[0]

            global fkMetricaLimiteFrequenciaCpu
            fkMetricaLimiteFrequenciaCpu = resultado[2]


def criacaoVariaveisMetricaRam(metricas):
    global limiteGbRam
    limiteGbRam = metricas[0][0]

    global fkMetricalimiteGbRam
    fkMetricalimiteGbRam = metricas[0][1]


def criacaoVariaveisMetricaDisco(metricas):
    global limiteGbDisco
    limiteGbDisco = metricas[0][0]

    global fkMetricalimiteGbDisco
    fkMetricalimiteGbDisco = metricas[0][1]


# ================================================================= Menu inicial
def opcoesMenu():
       
    opcoesInicio = ['Verificar Dados', 'Configurações', 'Sair']
    opcaoEscolhida, index = pick(opcoesInicio, indicator='=>', default_index=0)

    if(opcaoEscolhida == 'Verificar Dados'):
        exibirDados()

    elif(opcaoEscolhida == 'Configurações'):
        opcoesExibicaoCaptura()


# ================================================================= Exibição dos dados
def exibirDados():   

    coletarDadosCpu()    
    coletarDadosDisco()
    coletarDadosRam()

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
                                    CPU
    ===========================================================================
            | Processadores físicos: {dadoCpuFisc}
            | Processadores Lógicos: {dadoCpuLogc}
            | Frequência da CPU: {dadoCpuFreq}MHz
            | Porcentagem de uso da CPU: {dadoCpuPercent} %
    ===========================================================================

                                    ARMAZENAMENTO
    ===========================================================================
            | Partições: {dadoHdNumParcs}
            | Armazenamento total: {dadoHdTotal} GB
            | Uso atual: {dadoHdAtual} GB
            | Porcentagem de uso: {dadoHdPercent} %
    ===========================================================================
 
                                     MEMÓRIA
    ===========================================================================
           | Quantidade total de RAM: {dadoRamTotal} GB
           | Uso atua de RAM: {dadoRamAtual} GB
           | Porcentagem de uso: {dadoRamPercent} %
    ===========================================================================

    (Pressione [ESC] para voltar)
                """)

    global tempoChamado    
    operacoesBanco.inserirFrequencia(dadoCpuFreq,limiteFrequenciaCpu,idCpu,idServidor,fkMetricaLimiteFrequenciaCpu,tempoChamado)

    if(platform.system() == 'Linux'):
        operacoesBanco.inserirTemperatura(dadoCpuTemperatura,limiteTemperaturaCpu,idCpu,idServidor,fkMetricaLimiteTemperaturaCpu,tempoChamado)

    operacoesBanco.inseritPorcentagemCpu(dadoCpuPercent,limiteUsoCpu,idCpu,idServidor,fkMetricaLimiteUsoCpu,tempoChamado)
    
    operacoesBanco.inserirHdAtual(dadoHdAtual,limiteGbDisco,idCpu,idServidor,fkMetricalimiteGbDisco,tempoChamado) 
    operacoesBanco.inserirRamAtual(dadoRamAtual,limiteGbRam,idCpu,idServidor,fkMetricalimiteGbRam,tempoChamado) 

    if tempoChamado <= 10:
    
        tempoChamado += 1
    
    else:
        tempoChamado = 1

    if k.read_key() == 'esc':
        opcoesMenu()
            
    else:
        t.sleep(1)
        exibirDados()

# ================================================================= Opcões de exibição de capturas
def opcoesExibicaoCaptura():
    opcoesConfig = ['CPU', 'HD', 'RAM', "Voltar"]
    opcoesHardware, index = pick(opcoesConfig, indicator='=>', default_index=0)

    if (opcoesHardware == 'CPU'):
        opcoesCPUConfig()

    elif(opcoesHardware == 'HD'):
        opcoesHDConfig()
    
    elif(opcoesHardware == 'RAM'):
        opcoesRAMConfig()
    
    else:
        opcoesMenu()


# ================================================================= Opções CPU
def opcoesCPUConfig():

    opcoesEscolha = [True, False]
    opcoesCPU = ['Processadores físicos', 'Processadores Lógicos', 'Frequência de CPU', 'Porcentagem de uso da CPU', 'Voltar']
    opcConfigCPU, index = pick(opcoesCPU, indicator='=>', default_index=0)

    if(opcConfigCPU == 'Processadores físicos'):
    
        opcoesEscolha, index = pick(opcoesEscolha, indicator='=>', default_index=0)
        user.CPUFisc = opcoesEscolha

        opcoesCPUConfig()

    elif(opcConfigCPU == 'Processadores Lógicos'):
        
        opcoesEscolha, index = pick(opcoesEscolha, indicator='=>', default_index=0)
        user.CPULogc = opcoesEscolha

        opcoesCPUConfig()

    elif(opcConfigCPU == 'Frequência de CPU'):
       
        opcoesEscolha, index = pick(opcoesEscolha, indicator='=>', default_index=0)
        user.CPUFreq = opcoesEscolha

        opcoesCPUConfig()

    elif(opcConfigCPU == 'Porcentagem de uso da CPU'):

        opcoesEscolha, index = pick(opcoesEscolha, indicator='=>', default_index=0)
        user.CPUPercent = opcoesEscolha

        opcoesCPUConfig()

    else:
        opcoesExibicaoCaptura()    


# ================================================================= Opções HD
def opcoesHDConfig():
    opcoesEscolha = [True, False]    
    opcoesHD = ['Partições do HD', 'Armazenamento total', 'Armazenamento atual', 'Porcentagem de uso do HD', 'Voltar']
    opcConfigHD, index = pick(opcoesHD, indicator='=>', default_index=0)

    if(opcConfigHD == 'Partições do HD'):

        opcoesEscolha, index = pick(opcoesEscolha, indicator='=>', default_index=0)
        user.HDNumParcs = opcoesEscolha

        opcoesHDConfig()

    elif(opcConfigHD == 'Armazenamento total'):
        
        opcoesEscolha, index = pick(opcoesEscolha, indicator='=>', default_index=0)
        user.HDTotal = opcoesEscolha

        opcoesHDConfig()

    elif(opcConfigHD == 'Armazenamento atual'):

        opcoesEscolha, index = pick(opcoesEscolha, indicator='=>', default_index=0)
        user.HDAtual = opcoesEscolha
        
        opcoesHDConfig()

    elif(opcConfigHD == 'Porcentagem de uso do HD'):

        opcoesEscolha, index = pick(opcoesEscolha, indicator='=>', default_index=0)
        user.HDPercent = opcoesEscolha

        opcoesHDConfig()

    else:
        opcoesExibicaoCaptura()   


# ================================================================= Opções RAM
def opcoesRAMConfig():

    opcoesEscolha = [True, False]  
    opcoesRAM = ['Quantidade total de RAM', 'Uso atual de RAM', 'Porcentagem de uso da RAM', 'Voltar']
    opcConfingRAM, index = pick(opcoesRAM, indicator='=>', default_index=0)

    if(opcConfingRAM == 'Quantidade total de RAM'):
    
        opcoesEscolha, index = pick(opcoesEscolha, indicator='=>', default_index=0)         
        user.RAMTot = opcoesEscolha

        opcoesRAMConfig()

    elif(opcConfingRAM == 'Uso atual de RAM'):
        
        opcoesEscolha, index = pick(opcoesEscolha, indicator='=>', default_index=0)
        user.RAMAtual = opcoesEscolha

        opcoesRAMConfig()

    elif(opcConfingRAM == 'Porcentagem de uso da RAM'):
      
        opcoesEscolha, index = pick(opcoesEscolha, indicator='=>', default_index=0)
        user.RAMPercent = opcoesEscolha

        opcoesRAMConfig()

    else:
        opcoesExibicaoCaptura()   

    
# ================================================================= Coleta de dados
def coletarDadosCpu():

    global dadoCpuFisc
    dadoCpuFisc = ps.cpu_count(False) if user.CPUFisc else None
    
    global dadoCpuLogc
    dadoCpuLogc = ps.cpu_count(True) if user.CPULogc else None
    
    global dadoCpuFreq
    dadoCpuFreq = round(ps.cpu_freq(False).current, 2) if user.CPUFreq else None
    
    global dadoCpuPercent
    dadoCpuPercent = round(ps.cpu_percent(), 2) if user.CPUPercent else None
    
    
    if(platform.system() == 'Linux'):
        global dadoCpuTemperatura
        dadoCpuTemperatura = ps.sensors_temperatures(fahrenheit=False)

def coletarDadosDisco():
    global disks
    disks = ps.disk_partitions()

    global dadoHdNumParcs
    dadoHdNumParcs = len(disks) if user.HDNumParcs else None

    global dadoHdTotal
    dadoHdTotal = round((ps.disk_usage("/").total)*10**-9,2) if user.HDTotal else None
    
    global dadoHdAtual
    dadoHdAtual = round((ps.disk_usage("/").used)*10**-9,2) if user.HDAtual else None
    
    global dadoHdPercent
    dadoHdPercent = ps.disk_usage("/").percent if user.HDPercent else None


def coletarDadosRam():
    global dadoRamTotal
    dadoRamTotal = round((ps.virtual_memory().total)*10**-9,2) if user.RAMTot else None

    global dadoRamAtual
    dadoRamAtual = round((ps.virtual_memory().used)*10**-9,2) if user.RAMAtual else None
    
    global dadoRamPercent
    dadoRamPercent = ps.virtual_memory().percent if user.RAMPercent else None

loginUsuario()