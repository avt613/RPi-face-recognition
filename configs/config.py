from cs50 import SQL
db = SQL('sqlite:///faces.db')
query = db.execute("SELECT * FROM settings ORDER BY id")
for i in range(len(query)):
    exec(query[i]['name'] + " = query[i]['value']")

import socket
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

webaddress = 'http://' + get_ip_address()
