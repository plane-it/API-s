import mysql.connector
import pyodbc

# # MYSQL LOCAL
# DB = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="lucas-00123969130980362",
#     database="planeit"
# )

# mycursor = DB.cursor()
# #

server = '44.218.73.236'
database = 'planeit'
username = 'planeit'
password = 'planeit123'
port = '1433'  # Porta padrão do SQL Server

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = conn.cursor()

