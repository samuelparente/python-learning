# Samuel Parente - Python programming exercises

import mysql.connector

# Connect to mysql server
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="python_database_test"
)

mycursor = mydb.cursor()

# Create a new database
# mycursor.execute("CREATE DATABASE python_database_test")

# Create a new table
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# Insert some data
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
          ('João', 'Porto'),
          ('Maria', 'Braga'),
          ('Artur', 'Vila Nova de Gaia'),
          ('José', 'Portimão'),
          ('Samuel', 'Celorico de Basto'),
          ('Sara', 'Lisboa'),
          ('Susana', 'Faro'),
          ('Ricardo', 'Viana do Castelo'),
          ('Benjamim', 'Aveiro')
]

mycursor.executemany(sql, val)
mydb.commit()

# Just outputs the number of registers inserted
print(mycursor.rowcount, "registers were inserted.")

# Reads all data from the selected table and outputs it
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
