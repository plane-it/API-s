import requests
import json
import datetime as dt
import csv as CSV
import mysql.connector as mysql

pool = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'sherlock15!',
    database = 'planeit '
)

current_time = dt.datetime.now()
global yearData
global monthData
yearData = current_time.year
monthData = current_time.month

def isJson(text):
    try:
        json.loads(text)
        return True
    except:
        return False

def loadsData(year, month):

    global yearData
    global monthData

    print("Exibindo year e month")
    print(year, month)

    if (month == monthData):
        month -= 1
        print(month)
        if (month == 0):
            return
    

    filename = 'flyesMonth{year}_{month:0>2}.csv'.format(year = year, month = month)
    CSV_URL="https://www.gov.br/anac/pt-br/assuntos/dados-e-estatisticas/percentuais-de-atrasos-e-cancelamentos-2/{year}/vra_{year}_{month:0>2}.csv".format(year = year, month = month)
    with requests.Session() as s:
            print("dentro do request")

            download = s.get(CSV_URL) 
            if(isJson(download.content)):
                print("é json")
                monthData -= 1
                loadsData(year, month)
            else: 
                print("Downloaded file: {filename}".format(filename = filename))
                monthData -= 1
                print(yearData, monthData, year, month)
                with open( filename, 'wb') as f:
                    print("arquivo foi aberto")
                    f.write(download.content)

loadsData(yearData, monthData)
    
def splitValues(row):
    return row.split(';')
print("aqui")

def flatten(l):
    return [item for sublist in l for item in sublist]
print("aqui1")

global lastDatetime
lastDatetime = ""
def formatToDate(data):
    global lastDatetime
    date = dt.datetime.now()
    if(data == '' or type(data) != str):
        date = dt.datetime.strptime(lastDatetime, "%d/%m/%Y %H:%M")
    else:
        lastDatetime = data
        date = dt.datetime.strptime(data, "%d/%m/%Y %H:%M")
    return date.strftime("%Y-%m-%d %H:%M:%S")
print("aqui2")
print(yearData, monthData)
with open('flyesMonth{yearData}_{monthData:0>2}.csv'.format(yearData=yearData, monthData=monthData), 'r') as file:
    print("arquivo aberto")
    rows = file.read().split('\n')
    columns = list(map(splitValues, rows))

    cursor = pool.cursor()
    cursor.execute("call deleteByMonth({yearData},{monthData})".format(yearData=yearData, monthData=monthData))
    pool.commit()
    for column in columns[1:len(columns)-2]:
        
        newColumn = flatten([column[0:2],column[4:5],list(map(formatToDate,column[5:7])), column[7:8], list(map(formatToDate, column[8:10])), column[10:11]])

        cursor = pool.cursor()
        cursor.execute("""
        INSERT INTO voos
            (siglaEmpresaAerea, nVoo, siglaAeroportoOrigem, horaPartidaPrevista, horaPartidaReal, siglaAeroportoDestino, horaChegadaPrevista, horaChegadaReal, situacao)
        VALUES {col}""".format(col = tuple(newColumn)))
        pool.commit()

    if(monthData != 0):
        print("chamando o próximo mês")

        loadsData(yearData, monthData)
