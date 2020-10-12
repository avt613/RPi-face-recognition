from configs.config import db, timedelay
from datetime import timedelta, datetime
from time import sleep

def checkcamera(checkid):
    for i in range(2*int(timedelay)):
        last_ids = []
        times = ""
        for j in range(int(timedelay)):
            if j > 0:
                times = times + ", "
            times = times + "'" + (datetime.now() - timedelta(seconds=j)).strftime("%Y-%m-%d %H:%M:%S") + "'"
        query = db.execute("SELECT person_id FROM log WHERE datetime IN(" + times + ") GROUP BY person_id ORDER BY datetime DESC")
        for person in query:
            last_ids.append(int(person['person_id']))
        if int(checkid) in last_ids:
            return True
        sleep(0.25)
    return False
