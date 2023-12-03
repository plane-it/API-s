import wget;
import zipfile as zfile;
import datetime as dt;
from datetime import datetime
import mysql.connector as mysql;
import pandas as pd
import os
import pymssql
from statsmodels.tsa.arima.model import ARIMA



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
    path = f'{ano}'
    print("Separando os arquivos por regiões do Brasil")
    for i in os.listdir(path):
        arquivos = os.path.join(path,i)
        if "INMET_SE" in arquivos:
            inserirDados = """
                INSERT INTO tbSudeste(
                        localizacao,regiao,dataCompleta,precipitacao)
                VALUES (%s,%s,%s,%s)
                """
        elif "INMET_S" in arquivos:
            inserirDados = """
                INSERT INTO tbSul(
                        localizacao,regiao,dataCompleta,precipitacao)
                VALUES (%s,%s,%s,%s)
            """
        elif "INMET_CO" in arquivos:
            inserirDados = """
                INSERT INTO tbCentroOeste(
                        localizacao,regiao,dataCompleta,precipitacao)
                VALUES (%s,%s,%s,%s)
            """
        elif "INMET_NE" in arquivos:
            inserirDados = """
                INSERT INTO tbNordeste(
                        localizacao,regiao,dataCompleta,precipitacao)
                VALUES (%s,%s,%s,%s)
            """
        elif "INMET_N" in arquivos:
            inserirDados = """
                INSERT INTO tbNorte(
                        localizacao,regiao,dataCompleta,precipitacao)
                VALUES (%s,%s,%s,%s)
            """

        with open(arquivos,'r') as file:
            leitor = file.read().split("\n")
            regiao = leitor[1]
            localRegiao = regiao[4:6] 
            estacao = leitor[2]
            localEstacao = estacao[9:]

            maiorPrecipitacao = 0
            for index, idx in enumerate(leitor[10:len(leitor)-2]):
                linha = idx.split(";")

                if linha != ['']:
                    precipitacao = linha[2].replace(",",".")
                    if(index == 0 or linha[0] == leitor[index+9].split(";")[0]):
                        if(precipitacao != '' and float(precipitacao) > maiorPrecipitacao):
                            maiorPrecipitacao = float(precipitacao)
                    else:
                        dataArrumada = datetime.strptime(str(linha[0]), "%Y/%m/%d")
                        if maiorPrecipitacao != 0:
                            valores = (localEstacao,localRegiao,dataArrumada,maiorPrecipitacao)
                            cursor = conexao.cursor()
                            cursor.execute(inserirDados,valores)
                            conexao.commit()
                        maiorPrecipitacao = 0

def previsaoPorregiao(conexao, consulta):

    cursor = conexao.cursor()

    # Execute a consulta para obter os dados da tabela tbNordeste
    cursor.execute(consulta)
    rows = cursor.fetchall()

    # Crie um DataFrame com os dados
    df = pd.DataFrame(rows, columns=[i[0] for i in cursor.description])

    # Converta a coluna dataCompleta para o tipo de data
    df['dataCompleta'] = pd.to_datetime(df['dataCompleta'], format='%m-%d')
    print("arrumando a data")
    # print(df['dataCompleta'])

    # Ajustando o modelo ARIMA
    modelo = ARIMA(df['precipitacao'], order=(2,1,0))
    print(len(df['precipitacao']))
    modelo_ajustado = modelo.fit()
    print("modelo arima criado")

    inicio = 0
    fim = len(df)-1

    previsao = modelo_ajustado.predict(start=inicio, end=fim)

    # Cria um novo DataFrame para as previsões
    df['previsao'] = pd.DataFrame(previsao)

    # # Concatena o DataFrame original com o novo DataFrame de previsões
    # df_completo = pd.concat([df, df_previsao])


    print(df)

    # # Calcule a média dos valores de precipitacao agrupados por regiao e dataCompleta
    # df_avg = df.groupby(['regiao', 'dataCompleta'])['precipitacao'].mean().reset_index()

    # # Arredonde a coluna precipitacao para um decimal
    # df_avg['precipitacao'] = df_avg['precipitacao'].round(1)

    # # Insira os dados na tabela tbClimaEstado
    for i, row in df.iterrows():
        cursor.execute("INSERT INTO tbClimaEstado (regiao, dataCompleta, previsao) VALUES (%s, %s, %s)", (row['regiao'], row['dataCompleta'], row['previsao']))

    # Confirme as alterações
    conexao.commit()

anos = 2021
try:
    server = 'localhost'
    database = 'planeit'
    username = 'teste'
    password = '123'
    port = '1433'  # Default SQL Server port

    conexao = pymssql.connect(server=server, user=username, password=password, database=database, port=port)

    print('Conxeão estabelecida!')
    # while anos < tempo:
    #     findClima(anos)
    #     separateClima(anos)
    #     anos += 1

    consulta_Sudeste = "SELECT regiao, dataCompleta, precipitacao FROM tbSudeste ORDER BY regiao, dataCompleta;"
    # dadosSudeste = pd.read_sql(consulta_Sudeste, conexao)
    previsaoPorregiao(conexao, consulta_Sudeste)


    consulta_Sul = "SELECT regiao, dataCompleta, precipitacao FROM tbSul ORDER BY regiao, dataCompleta;"
    # dadosSul = pd.read_sql(consulta_Sul, conexao)
    previsaoPorregiao(conexao, consulta_Sul)


    consulta_CentroOeste = "SELECT regiao, dataCompleta, precipitacao FROM tbCentroOeste ORDER BY regiao, dataCompleta;"
    # dadosCentroOeste = pd.read_sql(consulta_CentroOeste, conexao)
    previsaoPorregiao(conexao, consulta_CentroOeste)


    consulta_Nordeste = "SELECT regiao, dataCompleta, precipitacao FROM tbNordeste ORDER BY regiao, dataCompleta;"
    # dadosNordeste = pd.read_sql(consulta_Nordeste, conexao)
    previsaoPorregiao(conexao, consulta_Nordeste)


    consulta_Norte = "SELECT regiao, dataCompleta, precipitacao FROM tbNorte ORDER BY regiao, dataCompleta;"
    # dadosNorte = pd.read_sql(consulta_Norte, conexao)
    previsaoPorregiao(conexao, consulta_Norte)
        
except Exception as error:
    print(f"Ocorreu um {error}")
finally:
    conexao.close()


 
    
