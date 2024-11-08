import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS Videogiochi")
mycursor.execute("USE Videogiochi")
mycursor.execute("CREATE TABLE games ( id INT AUTO_INCREMENT PRIMARY KEY, titolo VARCHAR(255),genere VARCHAR(255),piattaforma VARCHAR(255),data_uscita YEAR, sviluppatore VARCHAR(255))")

#crea il database e la table




