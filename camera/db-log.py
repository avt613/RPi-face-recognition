from config import db
from datetime import timedelta, datetime

times = ""
for i in range(10):
    if i > 0:
        times = times + ", "
    times = times + "'" + (datetime.now() - timedelta(seconds=i)).strftime("%Y-%m-%d %H:%M:%S") + "'"
query = db.execute("SELECT * FROM log WHERE datetime IN(" + times + ") GROUP BY name ORDER BY datetime DESC")
#query = db.execute("SELECT * FROM log ORDER BY datetime DESC LIMIT 10")
print("Name", ":" , "Date Time", ":" , "Distance")
for name in query:
    print(name['name'] , ":" , name['datetime'] , ":" , name['distance'])
