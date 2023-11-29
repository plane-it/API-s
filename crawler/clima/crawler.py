import wget;
import zipfile as zfile;
import datetime as dt;
from datetime import datetime
import csv;
import mysql.connector as mysql;
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm
import os



tempo = dt.datetime.now().year

def findClima(ano):
    url = f"https://portal.inmet.gov.br/uploads/dadoshistoricos/{ano}.zip"
    while ano <= tempo:
        if tempo != ano:
              print(f"\n Começando download do relatório do ano de {ano}")
              wget.download(url)
              print("Download finalizado")
              
              break
        else:
              break
        
    arquivoZip = f'{ano}.zip'
    with zfile.ZipFile(arquivoZip,'r') as z:
        print("Descompactando pasta")
        pastaExtraida = f'{ano}'
        z.extractall(pastaExtraida)
        print("Pasta extraída com sucesso")  

def separateClima(ano):
    sudeste= []
    nordeste = []
    norte = []
    sul = []
    centroOeste = []
    path = f'{ano}'
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

    dados_sudeste = []

    maiorPrecipitacao = 0
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
                    precipitacao = linha[2].replace(",",".") 
                    if precipitacao == '' or precipitacao == '0':
                        continue
                    if(float(precipitacao) > maiorPrecipitacao):
                            maiorPrecipitacao = float(precipitacao)
                            
                            linha_data =  str(linha[0])

                            # Convert the date string into a datetime object
                            dataArrumada = datetime.strptime(linha_data, "%Y/%m/%d")

                            # Extract the date part
                            dataArrumadaSemHora = dataArrumada.date()

                            # Extract the month and day
                            mesData = dataArrumadaSemHora.strftime("%m")
                            diaData = dataArrumadaSemHora.strftime("%d")

                            # Combine the month and day into a new date string
                            data = mesData + '-' + diaData                          

                            if precipitacao != '0':
                                inserirDados = """
                                INSERT INTO tbSudeste(
                                        localizacao,regiao,dataCompleta,precipitacao)
                                VALUES (%s,%s,%s,%s)
                                """
                                valores = (localEstacao,localRegiao,data,precipitacao)
                                cursor = conexao.cursor()
                                cursor.execute(inserirDados,valores)
                                conexao.commit() 
                               
        maiorPrecipitacao = 0
                    
    print('Dados enviados para a tabela tbSudeste')   



def sendDataSul(sul):
    maiorPrecipitacao = 0
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
                    precipitacao = linha[2].replace(",",".") 
                    if precipitacao == '' or precipitacao == '0':
                        continue
                    if(float(precipitacao) > maiorPrecipitacao):
                            maiorPrecipitacao = float(precipitacao)
                            
                            linha_data =  str(linha[0])

                            # Convert the date string into a datetime object
                            dataArrumada = datetime.strptime(linha_data, "%Y/%m/%d")

                            # Extract the date part
                            dataArrumadaSemHora = dataArrumada.date()

                            # Extract the month and day
                            mesData = dataArrumadaSemHora.strftime("%m")
                            diaData = dataArrumadaSemHora.strftime("%d")

                            # Combine the month and day into a new date string
                            data = mesData + '-' + diaData     
                    
                    if precipitacao != '0':
                        inserirDados = """
                        INSERT INTO tbSul(
                                localizacao,regiao,dataCompleta,precipitacao)
                        VALUES (%s,%s,%s,%s)
                        """
                        valores = (localEstacao,localRegiao,data,precipitacao)
                        cursor = conexao.cursor()
                        cursor.execute(inserirDados,valores)
                        conexao.commit() 
            maiorPrecipitacao = 0
                    
    print('Dados enviados para a tabela tbSul')

def sendDataCentro(centroOeste):
    maiorPrecipitacao = 0
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
                    precipitacao = linha[2].replace(",",".") 
                    if precipitacao == '' or precipitacao == '0':
                        continue
                    if(float(precipitacao) > maiorPrecipitacao):
                            maiorPrecipitacao = float(precipitacao)
                            
                            linha_data =  str(linha[0])

                            # Convert the date string into a datetime object
                            dataArrumada = datetime.strptime(linha_data, "%Y/%m/%d")

                            # Extract the date part
                            dataArrumadaSemHora = dataArrumada.date()

                            # Extract the month and day
                            mesData = dataArrumadaSemHora.strftime("%m")
                            diaData = dataArrumadaSemHora.strftime("%d")

                            # Combine the month and day into a new date string
                            data = mesData + '-' + diaData     

                
                    if precipitacao != '0':
                        inserirDados = """
                        INSERT INTO tbCentroOeste(
                                localizacao,regiao,dataCompleta,precipitacao)
                        VALUES (%s,%s,%s,%s)
                        """
                        valores = (localEstacao,localRegiao,data,precipitacao)
                        cursor = conexao.cursor()
                        cursor.execute(inserirDados,valores)
                        conexao.commit() 
            maiorPrecipitacao = 0
                    
    print('Dados enviados para a tabela tbCentroOeste') 

def sendDataNordeste(nordeste):
    maiorPrecipitacao = 0
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
                    precipitacao = linha[2].replace(",",".") 
                    if precipitacao == '' or precipitacao == '0':
                        continue
                    if(float(precipitacao) > maiorPrecipitacao):
                            maiorPrecipitacao = float(precipitacao)
                            
                            linha_data =  str(linha[0])

                            # Convert the date string into a datetime object
                            dataArrumada = datetime.strptime(linha_data, "%Y/%m/%d")

                            # Extract the date part
                            dataArrumadaSemHora = dataArrumada.date()

                            # Extract the month and day
                            mesData = dataArrumadaSemHora.strftime("%m")
                            diaData = dataArrumadaSemHora.strftime("%d")

                            # Combine the month and day into a new date string
                            data = mesData + '-' + diaData     

                
    

                    if precipitacao != '0':
                        inserirDados = """
                        INSERT INTO tbNordeste(
                                localizacao,regiao,dataCompleta,precipitacao)
                        VALUES (%s,%s,%s,%s)
                        """
                        valores = (localEstacao,localRegiao,data,precipitacao)
                        cursor = conexao.cursor()
                        cursor.execute(inserirDados,valores)
                        conexao.commit() 
            maiorPrecipitacao = 0
                    
    print('Dados enviados para a tabela tbNordeste') 

def sendDataNorte(norte):
    maiorPrecipitacao = 0

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
                    precipitacao = linha[2].replace(",",".") 
                    if precipitacao == '' or precipitacao == '0':
                        continue
                    if(float(precipitacao) > maiorPrecipitacao):
                            maiorPrecipitacao = float(precipitacao)
                            
                            linha_data =  str(linha[0])

                            # Convert the date string into a datetime object
                            dataArrumada = datetime.strptime(linha_data, "%Y/%m/%d")

                            # Extract the date part
                            dataArrumadaSemHora = dataArrumada.date()

                            # Extract the month and day
                            mesData = dataArrumadaSemHora.strftime("%m")
                            diaData = dataArrumadaSemHora.strftime("%d")

                            # Combine the month and day into a new date string
                            data = mesData + '-' + diaData     

                    
    

                    if precipitacao != '0':
                        inserirDados = """
                        INSERT INTO tbNorte(
                                localizacao,regiao,dataCompleta,precipitacao)
                        VALUES (%s,%s,%s,%s)
                        """
                        valores = (localEstacao,localRegiao,data,precipitacao)
                        cursor = conexao.cursor()
                        cursor.execute(inserirDados,valores)
                        conexao.commit() 
            maiorPrecipitacao = 0
                    
    print('Dados enviados para a tabela tbNorte')     


def previsaoPorregiao(conexao, consulta):

    cursor = conexao.cursor()

    # Execute a consulta para obter os dados da tabela tbNordeste
    cursor.execute(consulta)
    rows = cursor.fetchall()

    # Crie um DataFrame com os dados
    df = pd.DataFrame(rows, columns=[i[0] for i in cursor.description])

    # Converta a coluna dataCompleta para o tipo de data
    df['dataCompleta'] = pd.to_datetime(df['dataCompleta'], format='%m-%d')

    # Calcule a média dos valores de precipitacao agrupados por regiao e dataCompleta
    df_avg = df.groupby(['regiao', 'dataCompleta'])['precipitacao'].mean().reset_index()

    # Arredonde a coluna precipitacao para um decimal
    df_avg['precipitacao'] = df_avg['precipitacao'].round(1)

    # Insira os dados na tabela tbClimaEstado
    for i, row in df_avg.iterrows():
        cursor.execute("INSERT INTO tbClimaEstado (regiao, dataCompleta, previsao) VALUES (%s, %s, %s)", (row['regiao'], row['dataCompleta'], row['precipitacao']))

    # Confirme as alterações
    conexao.commit()

    
    
    




anos = 2021
try:
    conexao = mysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'sherlock15!',
        database = 'planeit',
        port = '3306'
    )
    if conexao.is_connected():
        print('Conxeão estabelecida!')
        # while anos < tempo:
        #     # findClima(anos)
        #     # separateClima(anos)
        #     anos += 1

        consulta_Sudeste = "SELECT regiao, dataCompleta, precipitacao FROM tbSudeste ORDER BY regiao, dataCompleta;"
        dadosSudeste = pd.read_sql(consulta_Sudeste, conexao)
        previsaoPorregiao(conexao, consulta_Sudeste)


        consulta_Sul = "SELECT regiao, dataCompleta, precipitacao FROM tbSul ORDER BY regiao, dataCompleta;"
        dadosSul = pd.read_sql(consulta_Sul, conexao)
        previsaoPorregiao(conexao, consulta_Sul)


        consulta_CentroOeste = "SELECT regiao, dataCompleta, precipitacao FROM tbCentroOeste ORDER BY regiao, dataCompleta;"
        dadosCentroOeste = pd.read_sql(consulta_CentroOeste, conexao)
        previsaoPorregiao(conexao, consulta_CentroOeste)


        consulta_Nordeste = "SELECT regiao, dataCompleta, precipitacao FROM tbNordeste ORDER BY regiao, dataCompleta;"
        dadosNordeste = pd.read_sql(consulta_Nordeste, conexao)
        previsaoPorregiao(conexao, consulta_Nordeste)


        consulta_Norte = "SELECT regiao, dataCompleta, precipitacao FROM tbNorte ORDER BY regiao, dataCompleta;"
        dadosNorte = pd.read_sql(consulta_Norte, conexao)
        previsaoPorregiao(conexao, consulta_Norte)
            
except Exception as error:
    print(f"Ocorreu um {error}")
finally:
    conexao.close()


 
    
