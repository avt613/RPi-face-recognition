from configs.config import db
from datetime import timedelta, datetime

def checkcamera(checkid):
    for i in range(int(timedelay)):
        last_ids = []
        times = ""
        for i in range(int(timedelay)):
            if i > 0:
                times = times + ", "
            times = times + "'" + (datetime.now() - timedelta(seconds=i)).strftime("%Y-%m-%d %H:%M:%S") + "'"
        query = db.execute("SELECT person_id FROM log WHERE datetime IN(" + times + ") GROUP BY person_id ORDER BY datetime DESC")
        for person in query:
            last_ids.append(int(person['person_id']))
        if int(checkid) in last_ids:
            return True
        time.sleep(0.5)          
    return False
