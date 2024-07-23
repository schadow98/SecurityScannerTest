import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('example.db')

# Ein Cursor-Objekt erstellen
cursor = conn.cursor()

# Sicheres Einfügen von Daten
name = 'John Doe'
age = 30
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))

# Sicheres Abfragen von Daten
user_id = 1
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
result = cursor.fetchone()
print(result)

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()
