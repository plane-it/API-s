import wget;
import zipfile as zfile;
import datetime as dt;
import csv;
import mysql.connector as mysql;
import os

tempo = dt.datetime.now().year
def findClima(ano):
      url = f"https://portal.inmet.gov.br/uploads/dadoshistoricos/{tempo}.zip"
      i = 1999
      while i <= tempo:
          if tempo == i:
              wget.download(url)
              print(f"\n Começando download do relatório do ano de {tempo}")
              print("Download finalizado")
              break
          else:
              print("Buscando anos anteriores")
              i+= 1
      arquivoZip = f'{tempo}.zip'
      with zfile.ZipFile(arquivoZip,'r') as z:
          print("Descompactando pasta")
          pastaExtraida = f'{tempo}'
          z.extractall(pastaExtraida)
          print("Pasta extraída com sucesso")  

def separateClima():
    sudeste= []
    nordeste = []
    norte = []
    sul = []
    centroOeste = []
    path = f'{tempo}'
    print("Separando os arquivos por regiões do Brasil")
    for i in os.listdir(path):
        arquivos = os.path.join(path,i)
        if "INMET_SE" in arquivos:
            sudeste.append(arquivos)
        elif "INMET_S" in arquivos:
            sul.append(arquivos)
        elif "INMET_CO" in arquivos:
            centroOeste.append(arquivos)
        elif "INMET_NE" in arquivos:
            nordeste.append(arquivos)
        elif "INMET_N" in arquivos:
            norte.append(arquivos)

    sendDataSudeste(sudeste)
    sendDataSul(sul)   
    sendDataCentro(centroOeste)
    sendDataNordeste(nordeste)
    sendDataNorte(norte)

def sendDataSudeste(sudeste):
    print('Tratando os dados de cada arquivo da região Sudeste')
    for i in sudeste:
        with open(i,'r') as file:
            leitor = file.read().split("\n")
            regiao = leitor[1]
            localRegiao = regiao[4:6] 
            estacao = leitor[2]
            localEstacao = estacao[9:]
            for idx in leitor[10:len(leitor)-2]:
                linha = idx.split(";")
                if linha != ['']:
                    data = linha[0]
                    horario = linha[1].replace(",",".") 
                    pressao = linha[3].replace(",",".")
                    temp = linha[7].replace(",",".")
                    tempor = linha[8].replace(",",".")
                    tempmx = linha[9].replace(",",".")
                    tempmn = linha[10].replace(",",".") 
                    umrel = linha[15].replace(",",".") 
                    arvel = linha[17].replace(",",".")

                    if pressao == '' or temp == '' or tempor == '' or tempmx == '' or tempmn == '' or umrel == '' or arvel == '':
                        continue
                        print(localRegiao,localEstacao,data,arvel)
    
                    inserirDados = """
                    INSERT INTO tbSudeste(
                            localizacao,regiao,dataCompleta,hora,pressaoAtm,temperaturaAr,temperaturaOrv,temperaturaMax,
                            temperaturaMin,umidadeRelativa,velocidadeAr
                    )
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
                    valores = (localEstacao,localRegiao,data,horario,pressao,temp,tempor,tempmx,tempmn,umrel,arvel)
                    cursor = conexao.cursor()
                    cursor.execute(inserirDados,valores)
                    conexao.commit() 
                    
    print('Dados enviados para a tabela tbSudeste')   

def sendDataSul(sul):
    for i in sul:
        with open(i,'r') as file:
            leitor = file.read().split("\n")
            regiao = leitor[1]
            localRegiao = regiao[4:6] 
            estacao = leitor[2]
            localEstacao = estacao[9:]
            for idx in leitor[10:len(leitor)-2]:
                linha = idx.split(";")
                if linha != ['']:
                    data = linha[0]
                    horario = linha[1].replace(",",".") 
                    pressao = linha[3].replace(",",".")
                    temp = linha[7].replace(",",".")
                    tempor = linha[8].replace(",",".")
                    tempmx = linha[9].replace(",",".")
                    tempmn = linha[10].replace(",",".") 
                    umrel = linha[15].replace(",",".") 
                    arvel = linha[17].replace(",",".")

                    if pressao == '' or temp == '' or tempor == '' or tempmx == '' or tempmn == '' or umrel == '' or arvel == '':
                        continue
                        print(localRegiao,localEstacao,data,arvel)
    
                    inserirDados = """
                    INSERT INTO tbSul(
                            localizacao,regiao,dataCompleta,hora,pressaoAtm,temperaturaAr,temperaturaOrv,temperaturaMax,
                            temperaturaMin,umidadeRelativa,velocidadeAr
                    )
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
                    valores = (localEstacao,localRegiao,data,horario,pressao,temp,tempor,tempmx,tempmn,umrel,arvel)
                    cursor = conexao.cursor()
                    cursor.execute(inserirDados,valores)
                    conexao.commit() 
                    
    print('Dados enviados para a tabela tbSul')

def sendDataCentro(centroOeste):
    for i in centroOeste:
        with open(i,'r') as file:
            leitor = file.read().split("\n")
            regiao = leitor[1]
            localRegiao = regiao[4:6] 
            estacao = leitor[2]
            localEstacao = estacao[9:]
            for idx in leitor[10:len(leitor)-2]:
                linha = idx.split(";")
                if linha != ['']:
                    data = linha[0]
                    horario = linha[1].replace(",",".") 
                    pressao = linha[3].replace(",",".")
                    temp = linha[7].replace(",",".")
                    tempor = linha[8].replace(",",".")
                    tempmx = linha[9].replace(",",".")
                    tempmn = linha[10].replace(",",".") 
                    umrel = linha[15].replace(",",".") 
                    arvel = linha[17].replace(",",".")

                    if pressao == '' or temp == '' or tempor == '' or tempmx == '' or tempmn == '' or umrel == '' or arvel == '':
                        continue
                        print(localRegiao,localEstacao,data,arvel)
    
                    inserirDados = """
                    INSERT INTO tbCentroOeste(
                            localizacao,regiao,dataCompleta,hora,pressaoAtm,temperaturaAr,temperaturaOrv,temperaturaMax,
                            temperaturaMin,umidadeRelativa,velocidadeAr
                    )
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
                    valores = (localEstacao,localRegiao,data,horario,pressao,temp,tempor,tempmx,tempmn,umrel,arvel)
                    cursor = conexao.cursor()
                    cursor.execute(inserirDados,valores)
                    conexao.commit() 
                    
    print('Dados enviados para a tabela tbCentroOeste') 

def sendDataNordeste(nordeste):
    for i in nordeste:
        with open(i,'r') as file:
            leitor = file.read().split("\n")
            regiao = leitor[1]
            localRegiao = regiao[4:6] 
            estacao = leitor[2]
            localEstacao = estacao[9:]
            for idx in leitor[10:len(leitor)-2]:
                linha = idx.split(";")
                if linha != ['']:
                    data = linha[0]
                    horario = linha[1].replace(",",".") 
                    pressao = linha[3].replace(",",".")
                    temp = linha[7].replace(",",".")
                    tempor = linha[8].replace(",",".")
                    tempmx = linha[9].replace(",",".")
                    tempmn = linha[10].replace(",",".") 
                    umrel = linha[15].replace(",",".") 
                    arvel = linha[17].replace(",",".")

                    if pressao == '' or temp == '' or tempor == '' or tempmx == '' or tempmn == '' or umrel == '' or arvel == '':
                        continue
                        print(localRegiao,localEstacao,data,arvel)
    
                    inserirDados = """
                    INSERT INTO tbNordeste(
                            localizacao,regiao,dataCompleta,hora,pressaoAtm,temperaturaAr,temperaturaOrv,temperaturaMax,
                            temperaturaMin,umidadeRelativa,velocidadeAr
                    )
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
                    valores = (localEstacao,localRegiao,data,horario,pressao,temp,tempor,tempmx,tempmn,umrel,arvel)
                    cursor = conexao.cursor()
                    cursor.execute(inserirDados,valores)
                    conexao.commit() 
                    
    print('Dados enviados para a tabela tbNordeste') 

def sendDataNorte(norte):

    for i in norte:
        with open(i,'r') as file:
            leitor = file.read().split("\n")
            regiao = leitor[1]
            localRegiao = regiao[4:6] 
            estacao = leitor[2]
            localEstacao = estacao[9:]
            for idx in leitor[10:len(leitor)-2]:
                linha = idx.split(";")
                if linha != ['']:
                    data = linha[0]
                    horario = linha[1].replace(",",".") 
                    pressao = linha[3].replace(",",".")
                    temp = linha[7].replace(",",".")
                    tempor = linha[8].replace(",",".")
                    tempmx = linha[9].replace(",",".")
                    tempmn = linha[10].replace(",",".") 
                    umrel = linha[15].replace(",",".") 
                    arvel = linha[17].replace(",",".")

                    if pressao == '' or temp == '' or tempor == '' or tempmx == '' or tempmn == '' or umrel == '' or arvel == '':
                        continue
                        print(localRegiao,localEstacao,data,arvel)
    
                    inserirDados = """
                    INSERT INTO tbNorte(
                            localizacao,regiao,dataCompleta,hora,pressaoAtm,temperaturaAr,temperaturaOrv,temperaturaMax,
                            temperaturaMin,umidadeRelativa,velocidadeAr
                    )
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
                    valores = (localEstacao,localRegiao,data,horario,pressao,temp,tempor,tempmx,tempmn,umrel,arvel)
                    cursor = conexao.cursor()
                    cursor.execute(inserirDados,valores)
                    conexao.commit() 
                    
    print('Dados enviados para a tabela tbNorte')       

try:
    conexao = mysql.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'climaDados',
        port = '3306'
    )
    if conexao.is_connected():
        print('Conxeão estabelecida!')
        findClima(tempo)
        separateClima()
except Exception as error:
    print(f"Ocorreu um {error}")
finally:
    conexao.close()


 
    
