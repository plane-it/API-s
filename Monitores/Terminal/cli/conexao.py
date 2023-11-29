import mysql.connector
import pymssql

# # MYSQL LOCAL
# DB = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="lucas-00123969130980362",
#     database="planeit"
# )

# mycursor = DB.cursor()
# #

server = 'ec2-44-218-73-236.compute-1.amazonaws.com'
database = 'planeit'
username = 'planeit'
password = 'planeit123'
port = '1433'  # Default SQL Server port

DB = pymssql.connect(server=server, user=username, password=password, database=database, port=port)

mycursor = DB.cursor()
