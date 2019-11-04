import mysql.connector
db_connection = mysql.connector.connect(
  host="127.0.0.1",
  user="fm",
  passwd="password"
)
print(db_connection)