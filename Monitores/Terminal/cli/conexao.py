import mysql.connector

DB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0108Oliver",
    database="planeit"
)

mycursor = DB.cursor()
