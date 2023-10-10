from tkinter import *
from tkinter.ttk import *
from time import sleep as s
import psutil as ps
import mysql.connector

DB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="planeit"
)

mycursor = DB.cursor()

root = Tk()
root.title("Monitor de Performance")
root.resizable(False,False)
# root.iconbitmap("assets/favicon.ico")

# Informações do usuário ===============================================
containerInfos = LabelFrame(root, text="Informações do sistema operacional")
containerInfos.grid(column=0,row=0,padx=20,pady=30)

containerUser = LabelFrame(containerInfos, text="Informações de usuário")
containerUser.grid(column=0,row=0)
lbUsuario = Label(containerUser, text=("Usuário atual: "+ps.users()[0].name))
lbUsuario.pack()

# Informações da máquina (PRINCIPAL) ===============================================
containerDesemp = LabelFrame(containerInfos, text="Informações de desempenho")
containerDesemp.grid(column=0,row=1)

# Configurações ===============================================
containerOpt = LabelFrame(containerInfos,  text="Opções")
containerOpt.grid(column=0,row=2)

containerTempoAtualiz = LabelFrame(containerOpt, text="Tempo de atualização dos dados (em segundos)")
containerTempoAtualiz.pack()

tempoAtualizacao = StringVar()
cmbTempoAtualiz = Combobox(containerTempoAtualiz, textvariable=tempoAtualizacao)
cmbTempoAtualiz["values"] = ("1","3","5","10","15")
cmbTempoAtualiz["state"] = "readonly"
cmbTempoAtualiz.set(cmbTempoAtualiz["values"][0])
cmbTempoAtualiz.pack()

# Campos da estrutura do desempenho ===============================================
colunas = ("CPU","Disco","Memória RAM")

infos = (
("Processadores físicos","Processadores lógicos","Frequência","Percentual de uso"),
("Número de partições","Total","Uso atual","Percentual de uso"),
("Total","Uso atual","Percentual de uso"))

CPUFisc = StringVar()
CPULogc = StringVar()
CPUFreq = StringVar()
CPUPercent = StringVar()

HDNumParcs = StringVar()
HDTotal = StringVar()
HDAtual = StringVar()
HDPercent = StringVar()

RAMTot = StringVar()
RAMAtual = StringVar()
RAMPercent = StringVar()

dados = ((CPUFisc,CPULogc,CPUFreq,CPUPercent),(HDNumParcs,HDTotal,HDAtual,HDPercent),(RAMTot,RAMAtual,RAMPercent))

indiceGrid = 0
for coluna in colunas:
    div = LabelFrame(containerDesemp,text=coluna)
    div.grid(column=indiceGrid,row=0,ipadx=0,ipady=0)

    i=0
    for info in infos[indiceGrid]:
        divInfo = LabelFrame(div,text=info)
        lbDado = Label(divInfo,textvariable=dados[indiceGrid][i])
        divInfo.pack()
        lbDado.pack()
        i += 1
    
    indiceGrid += 1

# ================================================================= Funções de inserção no banco 
def inserirBancoCPU(dadoCPUFisc,dadoCPULogc,dadoCPUFreq,dadoCPUPercent):
    
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoCPUFisc,1,1)

    mycursor.execute(sql, val)
    DB.commit()
    
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoCPULogc,1,1)
 
    mycursor.execute(sql,val)
    DB.commit()
    
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoCPUFreq,1,4)
  
    mycursor.execute(sql,val)
    DB.commit()
  
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoCPUPercent,1,4)

    mycursor.execute(sql,val)
    DB.commit() 


def inserirBancoHD(dadoHDNumParcs,dadoHDTotal,dadoHDAtual,dadoHDPercent):

    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoHDNumParcs,3,1)
       
    mycursor.execute(sql, val)
    DB.commit()
    
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoHDTotal,3,2)
 
    mycursor.execute(sql,val)
    DB.commit()
    
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoHDAtual,3,2)
  
    mycursor.execute(sql,val)
    DB.commit()
  
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoHDPercent,3,5)

    mycursor.execute(sql,val)
    DB.commit() 

def inserirBancoRam(dadoRAMTotal,dadoRAMAtual,dadoRAMPercent):
    
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoRAMTotal,2,1)
       
    mycursor.execute(sql, val)
    DB.commit()
    
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoRAMAtual,2,3)
 
    mycursor.execute(sql,val)
    DB.commit()
    
    sql = "INSERT INTO tbRegistro VALUES (null, %s, now(), %s, %s)"
    val = (dadoRAMPercent,2,3)
  
    mycursor.execute(sql,val)
    DB.commit()
  


# Renderização da parte gráfica =================================================================
while(True):
    dadoCPUFisc = ps.cpu_count(False)
    dadoCPULogc = ps.cpu_count(True)
    dadoCPUFreq = round(ps.cpu_freq(False).current, 2)
    dadoCPUPercent = round(ps.cpu_percent(), 2)

    disks = ps.disk_partitions()
    dadoHDNumParcs = len(disks)
    dadoHDTotal = round((ps.disk_usage("/").total)*10**-9,2)
    dadoHDAtual = round((ps.disk_usage("/").used)*10**-9,2) 
    dadoHDPercent = ps.disk_usage("/").percent

    dadoRAMTotal = round((ps.virtual_memory().total)*10**-9,2)
    dadoRAMAtual = round((ps.virtual_memory().used)*10**-9,2)
    dadoRAMPercent = ps.virtual_memory().percent

    dados[0][0].set(str(dadoCPUFisc))
    dados[0][1].set(str(dadoCPULogc))
    dados[0][2].set(str(dadoCPUFreq)+"MHz")
    dados[0][3].set(str(dadoCPUPercent)+"%")

    dados[1][0].set(str(dadoHDNumParcs))
    dados[1][1].set(str(dadoHDTotal)+"GB")
    dados[1][2].set(str(dadoHDAtual)+"GB")
    dados[1][3].set(str(dadoHDPercent)+"%")
    
    dados[2][0].set(str(dadoRAMTotal)+"GB")
    dados[2][1].set(str(dadoRAMAtual)+"GB")
    dados[2][2].set(str(dadoRAMPercent)+"%")
    root.update()
    s(int(tempoAtualizacao.get()))

    inserirBancoCPU(dadoCPUFisc,dadoCPULogc,dadoCPUFreq,dadoCPUPercent)
    inserirBancoHD(dadoHDNumParcs,dadoHDTotal,dadoHDAtual,dadoHDPercent)
    inserirBancoRam(dadoRAMTotal,dadoRAMAtual,dadoRAMPercent)
