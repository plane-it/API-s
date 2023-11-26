import wget;
import zipfile as zfile;
import datetime as dt;
import csv;
import mysql.connector as mysql;
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
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
                            data = linha[0]
                       

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
                            data = linha[0]
                    
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
                            data = linha[0]

                
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
                            data = linha[0] 

                
    

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
                            data = linha[0]

                    
    

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


def previsaoPorregiao(dados):

    dados_agrupado = []
    dados_agrupado = dados
    # Agrupar por 'regiao' e 'dataCompleta', calcular a média e contar
    dados_agrupado = dados.groupby(['regiao', 'dataCompleta'], as_index=False).agg({'precipitacao': ['mean', 'count']})

    # Renomear as colunas para facilitar o acesso
    dados_agrupado.columns = ['regiao', 'dataCompleta', 'mean', 'count']

    # Criar uma nova coluna com a precipitação média ou o valor original, dependendo da contagem
    dados_agrupado['mean'] = dados_agrupado.apply(lambda row: round(row['mean'], 1) if row['count'] == 1 else round(row['mean'], 1), axis=1)

    # Remover colunas temporárias
    dados_agrupado = dados_agrupado.drop(['count'], axis=1)
    

    for index, row in dados_agrupado.iterrows():
        
        regiao = row['regiao']
        dataCompleta = row['dataCompleta']
        previsao = row['mean']

        # Query SQL de inserção
        query = """
                    INSERT INTO tbClimaEstado (
                        regiao, dataCompleta, previsao) 
                        VALUES (%s, %s, %s)
                        """

        valores = (regiao,dataCompleta,previsao)
            # Executar a query
        cursor = conexao.cursor()
        cursor.execute(query, valores)
        conexao.commit() 

    
    
    print(dados_agrupado)  




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
        while anos < tempo:
            findClima(anos)
            separateClima(anos)
            anos += 1

        consulta_Sudeste = "SELECT regiao, dataCompleta, precipitacao FROM tbSudeste ORDER BY regiao, MONTH(dataCompleta), DAY(dataCompleta)"
        dadosSudeste = pd.read_sql(consulta_Sudeste, conexao, parse_dates=['dataCompleta'])
        previsaoPorregiao(dadosSudeste)


        consulta_Sul = "SELECT regiao, dataCompleta, precipitacao FROM tbSul ORDER BY regiao, MONTH(dataCompleta), DAY(dataCompleta)"
        dadosSul = pd.read_sql(consulta_Sul, conexao, parse_dates=['dataCompleta'])
        previsaoPorregiao(dadosSul)


        consulta_CentroOeste = "SELECT regiao, dataCompleta, precipitacao FROM tbCentroOeste ORDER BY regiao, MONTH(dataCompleta), DAY(dataCompleta)"
        dadosCentroOeste = pd.read_sql(consulta_CentroOeste, conexao, parse_dates=['dataCompleta'])
        previsaoPorregiao(dadosCentroOeste)


        consulta_Nordeste = "SELECT regiao, dataCompleta, precipitacao FROM tbNordeste ORDER BY regiao, MONTH(dataCompleta), DAY(dataCompleta)"
        dadosNordeste = pd.read_sql(consulta_Nordeste, conexao, parse_dates=['dataCompleta'])
        previsaoPorregiao(dadosNordeste)


        consulta_Norte = "SELECT regiao, dataCompleta, precipitacao FROM tbNorte ORDER BY regiao, MONTH(dataCompleta), DAY(dataCompleta)"
        dadosNorte = pd.read_sql(consulta_Norte, conexao, parse_dates=['dataCompleta'])
        previsaoPorregiao(dadosNorte)
            
except Exception as error:
    print(f"Ocorreu um {error}")
finally:
    conexao.close()


 
    
