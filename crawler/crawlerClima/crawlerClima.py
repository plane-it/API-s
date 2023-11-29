import requests
import bs4
import csv as CSV
import mysql.connector as mysql

try:
    pool = mysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'sherlock15!',
        database = 'planeit'
    ) 
    if pool.is_connected():
        print('Conxeão estabelecida!')
except Exception as error:
        print(f"Ocorreu um {error}")

url = "https://www.datascomemorativas.me/2023/feriados"

response = requests.get(url)

holidays_month = bs4.BeautifulSoup(response.text, "html.parser").find_all("div", class_="holidays")

holidays_list = bs4.BeautifulSoup(response.text, "html.parser").find_all("ul", class_="holidays-list")

vectorMeses = []
vectorDias  = []
vectorDiasSemana = []
vectorTitulos  = []
vectorTotais = []
diaMes = []
semanaMes = []
tituloMes = []
quantidadeMes = []


def getMeses():

    meses = {
    "Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Junho": 6,
    "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12
    }

    for month in holidays_month:
        # Extraia o nome do produto

        nomeMes = month.find_all("span", class_ = "holidays-month")

        for mes in nomeMes:
            nomeDoMes = mes.text
            numero_do_mes = meses.get(nomeDoMes, None)
            if numero_do_mes is not None:
                vectorMeses.append(numero_do_mes)
            else:
                print("Mês inválido")


def quantidadeFeriadosMes(conjuntoQuantidade):
    qtd = 0
    for quantidade in conjuntoQuantidade:
        qtd+=1
    quantidadeMes.append(qtd)
def getDias(conjuntoDias):
    for dia in conjuntoDias:
        vectorDias.append(dia.text)
    

def getDiasSemana(conjuntoSemana):
    for semana in conjuntoSemana:
        vectorDiasSemana.append(semana.text)

def getTitulos(conjuntoTitulos):
    for titulo in conjuntoTitulos:
        vectorTitulos.append(titulo.text)

def getBase():
    
    for date in  holidays_list:
        diaMes = date.find_all("span", class_ = "holiday-day")
        diaSemana = date.find_all("span", class_ = "holiday-dayoftheweek")
        conjuntoQuantidade = date.find_all("li", class_ = "holiday")
        tituloMes = date.find_all("a")
        quantidadeFeriadosMes(conjuntoQuantidade)
        getDias(diaMes)
        getDiasSemana(diaSemana)
        getTitulos(tituloMes)
    getMeses()

    index = 0 
    for id,i in enumerate(quantidadeMes):
        for _ in range(i):
            print(vectorMeses[id],vectorTitulos[index], vectorDias[index], vectorDiasSemana[index])
    
            inserirDados = """
                            INSERT INTO tbFeriados(
                                    dia,diaSemana,mes,titulo) VALUES (%s,%s,%s,%s)
                            """
            valores = (vectorDias[index],vectorDiasSemana[index], vectorMeses[id],vectorTitulos[index])
            cursor = pool.cursor()
            cursor.execute(inserirDados,valores)
            pool.commit() 
            index += 1
        

getBase()