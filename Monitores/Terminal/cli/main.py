import usuario
import psutil as ps
from pick import pick
import os
import time as t
import keyboard as k
import mysql.connector
from dotenv import load_dotenv
from getpass import getpass
import platform


# ================================================================= Carregando variaveis de ambiente
load_dotenv()

# ================================================================= Conexão mysql

DB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0108Oliver",
    database="planeit"
)

mycursor = DB.cursor()

# ================================================================= Login do usuário
user = usuario.Usuario(
    input("Digite o email de usuário: "),
    getpass("Digite a sua senha: ")
)

mycursor.execute(f"SELECT * FROM tbColaborador WHERE email = '{user.usuario}' AND senha = '{user.senha}'") 
myresult = mycursor.fetchall()

isRunning = False

if len(myresult) > 0:
    isRunning = True
else:
    print("Erro: Usuário não encontrado!")

# ================================================================= Funções de inserção no banco 
def inserirBancoCPU(dadoCPUFisc,dadoCPULogc,dadoCPUFreq,dadoCPUPercent):
    
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoCPUFisc,1,1,1)

    mycursor.execute(sql, val)
    DB.commit()
    
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoCPULogc,1,1,1)
 
    mycursor.execute(sql,val)
    DB.commit()
    
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoCPUFreq,1,1,1)
  
    mycursor.execute(sql,val)
    DB.commit()
  
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoCPUPercent,1,1,1)

    mycursor.execute(sql,val)
    DB.commit() 

    if(platform.uname().system != 'Windows'):
        sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
        val = (ps.sensors_temperatures(fahrenheit=False),1,1,1)

        mycursor.execute(sql,val)
        DB.commit()    

def inserirBancoHD(dadoHDNumParcs,dadoHDTotal,dadoHDAtual,dadoHDPercent):

    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoHDNumParcs,3,1,1)
       
    mycursor.execute(sql, val)
    DB.commit()
    
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoHDTotal,3,1,1)
 
    mycursor.execute(sql,val)
    DB.commit()
    
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoHDAtual,3,1,1)
  
    mycursor.execute(sql,val)
    DB.commit()
  
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoHDPercent,3,1,1)

    mycursor.execute(sql,val)
    DB.commit() 

def inserirBancoRam(dadoRAMTotal,dadoRAMAtual,dadoRAMPercent):
    
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoRAMTotal,2,1,1)
       
    mycursor.execute(sql, val)
    DB.commit()
    
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoRAMAtual,2,1,1)
 
    mycursor.execute(sql,val)
    DB.commit()
    
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoRAMPercent,2,1,1)
  
    mycursor.execute(sql,val)
    DB.commit()
  

# ================================================================= Configurações do programa
while isRunning:
    opcoesInicio = ['Verificar Dados', 'Configurações', 'Sair']

    opcEscolhida, index = pick(opcoesInicio, indicator='=>', default_index=0)


# ================================================================= Captura de Dados 

    if(opcEscolhida == 'Verificar Dados'):
        while True:
            dadoCPUFisc = ps.cpu_count(False) if user.CPUFisc else None
            dadoCPULogc = ps.cpu_count(True) if user.CPULogc else None
            dadoCPUFreq = round(ps.cpu_freq(False).current, 2) if user.CPUFreq else None
            dadoCPUPercent = round(ps.cpu_percent(), 2) if user.CPUPercent else None

            disks = ps.disk_partitions()
            dadoHDNumParcs = len(disks) if user.HDNumParcs else None
            dadoHDTotal = round((ps.disk_usage("/").total)*10**-9,2) if user.HDTotal else None
            dadoHDAtual = round((ps.disk_usage("/").used)*10**-9,2) if user.HDAtual else None
            dadoHDPercent = ps.disk_usage("/").percent if user.HDPercent else None

            dadoRAMTotal = round((ps.virtual_memory().total)*10**-9,2) if user.RAMTot else None
            dadoRAMAtual = round((ps.virtual_memory().used)*10**-9,2) if user.RAMAtual else None
            dadoRAMPercent = ps.virtual_memory().percent if user.RAMPercent else None
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
                                    CPU
    ===========================================================================
            | Processadores físicos: {dadoCPUFisc}
            | Processadores Lógicos: {dadoCPULogc}
            | Frequência da CPU: {dadoCPUFreq}MHz
            | Porcentagem de uso da CPU: {dadoCPUPercent} %
    ===========================================================================
                
                                    ARMAZENAMENTO
    ===========================================================================
            | Partições: {dadoHDNumParcs}
            | Armazenamento total: {dadoHDTotal} GB
            | Uso atual: {dadoHDAtual} GB
            | Porcentagem de uso: {dadoHDPercent} %
    ===========================================================================
                
                                    MEMÓRIA
    ===========================================================================
            | Quantidade total de RAM: {dadoRAMTotal} GB
            | Uso atua de RAM: {dadoRAMAtual} GB
            | Porcentagem de uso: {dadoRAMPercent} %
    ===========================================================================

    (Pressione [ESC] para voltar)
                """)
    
            inserirBancoCPU(dadoCPUFisc,dadoCPULogc,dadoCPUFreq,dadoCPUPercent)
            inserirBancoHD(dadoHDNumParcs,dadoHDTotal,dadoHDAtual,dadoHDPercent)
            inserirBancoRam(dadoRAMTotal,dadoRAMAtual,dadoRAMPercent)
    
            if k.read_key() == 'esc':
                break

            t.sleep(1)

    
# ================================================================= Configurações

    elif (opcEscolhida == 'Configurações'):
        opcoesConfig = ['CPU', 'HD', 'RAM', "Voltar"]
        opcHardware, index = pick(opcoesConfig, indicator='=>', default_index=0)
        opcEscolha = ['True', 'False']

# ================================================================= CPU
    
        if (opcHardware == 'CPU'):
            opcoesCPU = ['Processadores físicos', 'Processadores Lógicos', 'Frequência de CPU', 'Porcentagem de uso da CPU', 'Voltar']
            opcConfigCPU, index = pick(opcoesCPU, indicator='=>', default_index=0)
        
            if(opcConfigCPU == 'Processadores físicos'):
                opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                
                if(opcEscolha == 'True'): 
                    user.CPUFisc = True
                else: user.CPUFisc = False
            
            elif(opcConfigCPU == 'Processadores Lógicos'):
                opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                            
                if(opcEscolha == 'True'): 
                    user.CPULogc = True
                else: user.CPULogc = False

            elif(opcConfigCPU == 'Frequência de CPU'):
                opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                            
                if(opcEscolha == 'True'): 
                    user.CPUFreq = True
                else: user.CPUFreq = False  

            elif(opcConfigCPU == 'Porcentagem de uso da CPU'):
                opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                            
                if(opcEscolha == 'True'): 
                    user.CPUPercent = True
                else: user.CPUPercent = False            

# ================================================================= HD

        elif(opcHardware == 'HD'):
            opcoesHD = ['Partições do HD', 'Armazenamento total', 'Armazenamento atual', 'Porcentagem de uso do HD', 'Voltar']
            opcConfigHD, index = pick(opcoesHD, indicator='=>', default_index=0)
            
            if(opcConfigHD == 'Partições do HD'):
                opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                
                if(opcEscolha == 'True'): 
                    user.HDNumParcs = True
                else: user.HDNumParcs = False

            elif(opcConfigHD == 'Armazenamento total'):
                opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                
                if(opcEscolha == 'True'): 
                    user.HDTotal = True
                else: user.HDTotal = False

            elif(opcConfigHD == 'Armazenamento atual'):
                opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                
                if(opcEscolha == 'True'): 
                    user.HDAtual = True
                else: user.HDAtual = False
                
            elif(opcConfigHD == 'Porcentagem de uso do HD'):
                opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                
                if(opcEscolha == 'True'): 
                    user.HDPercent = True
                else: user.HDPercent = False

#======================================================================================== RAM
        elif(opcHardware == 'RAM'):
            opcoesRAM = ['Quantidade total de RAM', 'Uso atual de RAM', 'Porcentagem de uso da RAM', 'Voltar']
            opcConfingRAM, index = pick(opcoesRAM, indicator='=>', default_index=0)
            
            if(opcConfingRAM == 'Partições do HD'):
                opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                
                if(opcEscolha == 'True'): 
                    user.RAMTot = True
                else: user.RAMTot = False

            elif(opcConfingRAM == 'Uso atual de RAM'):
                opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                
                if(opcEscolha == 'True'): 
                    user.RAMAtual = True
                else: user.RAMAtual = False

            elif(opcConfingRAM == 'Porcentagem de uso da RAM'):
                opcEscolha, index = pick(opcEscolha, indicator='=>', default_index=0)
                
                if(opcEscolha == 'True'): 
                    user.RAMPercent = True
                else: user.RAMPercent = False


#====================================================================================== Sair

    elif(opcEscolhida == 'Sair'):
        break
