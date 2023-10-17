import mysql.connector


mydb = mysql.connector.connect(
  host="20.151.65.130",
  user="testing",
  password="example-pass",
  database="catraquiheights"
)

mycursor = mydb.cursor()
name = "testing"
mycursor.execute(f"CREATE TABLE {name} (name VARCHAR(255), address VARCHAR(255))")
