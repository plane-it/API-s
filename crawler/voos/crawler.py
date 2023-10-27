import wget;
import zipfile;
from datetime import datetime;
import csv;
import mysql.connector;
from pytz import timezone
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
            precipitacaoTot = linha[2]    
            pressaoAtm = linha[3]  
            tempAr = linha[7]
            tempOrvalho = linha[8]
            tempMax = linha[9]
            tempMin = linha[10]
            umidRel = linha[15]
            ventoVelocidade = linha[17]
        #Convertendo para o formato ideal para enviar para o banco
            conversaoPrecip = float(precipitacaoTot[0:4].replace(",",'.'))
            conversaoPress = float(pressaoAtm[0:4].replace(",",'.'))
            conversaoAr = float(tempAr[0:4].replace(",",'.'))
            conversaoOrv = float(tempOrvalho[0:4].replace(",",'.'))
            conversaoTempMax = float(tempMax[0:4].replace(",",'.'))
            conversaoTempMin = float(tempMin[0:4].replace(",",'.'))
            conversaoVelocidade = round((float(ventoVelocidade[0:4].replace(",",'.'))*3.6),1)
            conversaoData = datetime.strptime(data,"%Y/%m/%d").date()
            if(hora.find("UTC")):
                novahora = hora[0:3]
                intHora = int(novahora)
                hora_comum_sp = datetime.fromtimestamp(intHora,tz=timezone('America/Sao_Paulo'))
                horaConvertida = str(hora_comum_sp)
                horarioFormatado = horaConvertida[10:16]
            else:
                horarioFormatado = hora
        # conversaoHora = datetime.strptime(hora,formatacaoHora).strftime(formatto)
        #Print de todos os dados extraidos sem conversão
            print(f"A data foi: {data}")
            print(f"O horário foi: {hora}")
            print(f"A precipitação total :{precipitacaoTot} mm")
            print(f"A pressão atmosférica: {pressaoAtm} mB")
            print(f"A temperatura do ar seco: {tempAr} °C")
            print(f"A temperatura de Orvalho é: {tempOrvalho} °C")
            print(f"A temperatura máxima é : {tempMax} °C")
            print(f"A temperatura minima é : {tempMin} °C")
            print(f"A umidade relativa do ar: {umidRel} %")
            print(f"A velocidade do vento: {ventoVelocidade} m/s")
        #Inserindo no banco de dados
            inserirDados = """
            INSERT INTO tbClima (
                regiao,dataCompleta,hora,precipitacaoTotal,pressaoAtm,temperaturaAr,temperaturaOrv,temperaturaMax,temperaturaMin,umidadeRelativa,
                velocidadeAr
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            valores = (localRegiao,conversaoData,horarioFormatado,conversaoPrecip,conversaoPress,conversaoAr,conversaoOrv,conversaoTempMax,conversaoTempMin,umidRel,conversaoVelocidade)

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

# findClima(tempo)

 
    
