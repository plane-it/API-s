import requests
import bs4

url = "https://www.datascomemorativas.me/2023/feriados"

response = requests.get(url)

holidays_month = bs4.BeautifulSoup(response.text, "html.parser").find_all("div", class_="holidays")

holidays_list = bs4.BeautifulSoup(response.text, "html.parser").find_all("ul", class_="holidays-list")

vectorMeses = []
vectorDias  = []
vectorSemanas  = []
vectorTitulos  = []
vectorTotais = []
diaMes = []
semanaMes = []
tituloMes = []
quantidadeMes = []


def getMeses():
    for month in holidays_month:
        # Extraia o nome do produto

        nomeMes = month.find_all("span", class_ = "holidays-month")
        for mes in nomeMes:
            vectorMeses.append(mes.text)

def quantidadeFeriadosMes(conjuntoQuantidade):
    qtd = 0
    for quantidade in conjuntoQuantidade:
        qtd+=1
    quantidadeMes.append(qtd)
def getDias(conjuntoDias):
    for dia in conjuntoDias:
        vectorDias.append(dia.text)

def getSemanas(conjuntoSemanas):
    for semana in conjuntoSemanas:
        vectorSemanas.append(semana.text)

def getTitulos(conjuntoTitulos):
    for titulo in conjuntoTitulos:
        vectorTitulos.append(titulo.text)

def getBase():
    
    for date in  holidays_list:
        diaMes = date.find_all("span", class_ = "holiday-day")
        semanaMes = date.find_all("span", class_ = "holiday-dayoftheweek")
        conjuntoQuantidade = date.find_all("li", class_ = "holiday")
        tituloMes = date.find_all("a")
        quantidadeFeriadosMes(conjuntoQuantidade)
        getDias(diaMes)
        getSemanas(semanaMes)
        getTitulos(tituloMes)
    getMeses()

    index = 0 
    for id,i in enumerate(quantidadeMes):
        for _ in range(i):
            print(vectorMeses[id],vectorTitulos[index], vectorDias[index])
            index += 1
        

getBase()