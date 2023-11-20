import requests
import json
import datetime as dt
import csv as CSV
import mysql.connector as mysql

pool = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'sherlock15!',
    database = 'teste'
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
    filename = 'flyesMonth{year}_{month:0>2}.csv'.format(year = year, month = month)  
    CSV_URL="https://www.gov.br/anac/pt-br/assuntos/dados-e-estatisticas/percentuais-de-atrasos-e-cancelamentos-2/{year}/vra_{year}_{month:0>2}.csv".format(year = year, month = month)
    with requests.Session() as s:
        download = s.get(CSV_URL) 
        if(isJson(download.content)):
            newMonth = month - 1
            newYear = year
            if(newMonth == 0):
                newMonth = 12
                newYear -= 1
            
            yearData = newYear
            monthData = newMonth

            loadsData(newYear, newMonth)
        else: 
            print("Downloaded file: {filename}".format(filename = filename))
            print(yearData, monthData, year, month)
            with open( filename, 'wb') as f:
                f.write(download.content)

loadsData(yearData, monthData)
    
def splitValues(row):
    return row.split(';')

def flatten(l):
    return [item for sublist in l for item in sublist]

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

print(yearData, monthData)
with open('flyesMonth{yearData}_{monthData:0>2}.csv'.format(yearData=yearData, monthData=monthData), 'r') as file:
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
