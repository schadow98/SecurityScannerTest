import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('example.db')

# Ein Cursor-Objekt erstellen
cursor = conn.cursor()

# Sicheres Einfügen von Daten
name = 'John Doe'
age = 30
cursor.execute("INSERT INTO users (" + name + ", " + age + ") VALUES (?, ?)")

# Sicheres Abfragen von Daten
username  = "Malte"
password  = "TEST"
cmd = "SELECT * FROM Users WHERE Username = '" + username + "' AND Password = '"+ password + "'"

