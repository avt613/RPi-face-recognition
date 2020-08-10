from cs50 import SQL
db = SQL('sqlite:///faces.db')
query = db.execute("SELECT * FROM settings ORDER BY id")
for i in range(len(query)):
    exec(query[i]['name'] + " = query[i]['value']")
