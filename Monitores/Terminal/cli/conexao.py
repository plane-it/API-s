import mysql.connector

DB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="lucas-00123969130980362",
    database="planeit"
)

mycursor = DB.cursor()
