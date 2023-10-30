import wget;
import zipfile;
from datetime import datetime;
import csv;
import mysql.connector;
from pytz import timezone;
import time;

tempo = datetime.now().year
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
      with zipfile.ZipFile(arquivoZip,'r') as z:
          print("Descompactando pasta")
          pastaExtraida = f'{tempo}'
          z.extractall(pastaExtraida)
          print("Pasta extraída com sucesso")  

def readClima():
    with open(f'{tempo}/INMET_SE_SP_A771_SAO PAULO - INTERLAGOS_01-01-{tempo}_A_30-09-{tempo}.CSV','r') as c:
            leitura = c.read().split("\n")
            regiao = leitura[0]   
            localRegiao = regiao[8:10]
    for i in leitura[10:]:
        #Extraindo os dados do csv
            linha = i.split(";")
            data = linha[0]
            hora = linha[1]
            pressao = linha[3].replace(",",".")
            temp = linha[7].replace(",",".")
            tempOr = linha[8].replace(",",".")
            tempmx = linha[9].replace(",",".")
            tempmn = linha[10].replace(",",".")
            umrel = linha[15].replace(",",".")
            arvel = linha[17].replace(",",".")
            # if data == "2" and hoa == "1200 UTC":
            #     continue
            if pressao == "" or umrel == "" or arvel == "" or temp == "" or tempmx == "" or tempmn == "" or arvel == "":
                continue
            conversaoData = datetime.strptime(data,"%Y/%m/%d").date()
        # conversaoHora = datetime.strptime(hora,formatacaoHora).strftime(formatto)
        #Print de todos os dados extraidos sem conversão    
            print(f"A data foi: {data}")
            print(f"O horário foi: {hora}")
            print(f"A pressão atmosférica: {pressao} mB")
            print(f"A temperatura do ar seco: {temp} °C")
            print(f"A temperatura de Orvalho é: {tempOr} °C")
            print(f"A temperatura máxima é : {tempmx} °C")
            print(f"A temperatura minima é : {tempmn} °C")
            print(f"A umidade relativa do ar: {umrel} %")
            print(f"A velocidade do vento: {arvel} m/s")

        #Inserindo no banco de dados

            inserirDados = """
            INSERT INTO tbClima (
                regiao,dataCompleta,hora,pressaoAtm,temperaturaAr,temperaturaOrv,temperaturaMax,temperaturaMin,umidadeRelativa,
                velocidadeAr
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            valores = (localRegiao,conversaoData,hora,pressao,temp,tempOr,tempmx,tempmn,umrel,arvel)

            cursor = conexao.cursor()
            cursor.execute(inserirDados,valores)
            conexao.commit()       
try:
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'clubpenguim',
        database = 'climaDados',
        port = '3306'
    )
    if conexao.is_connected():
        print('Conxeão estabelecida!')
        findClima(tempo)
        readClima()
except Exception as error:
    print(f"Ocorreu um {error}")
finally:
    print("Dados enviados para o banco")
    conexao.close()


 
    
