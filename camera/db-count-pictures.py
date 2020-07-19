from config import db
print(db.execute("SELECT count(*) AS num FROM pictures")[0]["num"])

