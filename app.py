from flask import Flask, flash, redirect, render_template, request, url_for
from config import *

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

#--------------------------------
@app.route("/")
def index_page():
    return render_template("/index.html")

#--------------------------------
@app.route("/settings")
def settings_page():
    settings = db.execute("SELECT * FROM settings ORDER BY id ASC")
    return render_template("/settings.html", settings=settings)

@app.route("/settings/update", methods=["POST"])
def settings_update():
    setting_id = request.form.get("id")
    setting_name = request.form.get("name")
    setting_value = request.form.get("value")
    settings = db.execute("UPDATE settings SET name=?, value=? WHERE id=?", setting_name, setting_value, setting_id)
    exec(setting_name + " = setting_value")
    return redirect("/settings")

@app.route("/settings/delete", methods=["POST"])
def settings_delete():
    setting_id = request.form.get("id")
    setting_name = request.form.get("name")
    settings = db.execute("DELETE FROM settings WHERE id=?", setting_id)
    exec("del " + setting_name)
    return redirect("/settings")

@app.route("/settings/new", methods=["POST"])
def settings_new():
    setting_name = request.form.get("name")
    setting_value = request.form.get("value")
    settings = db.execute("INSERT INTO settings VALUES(NULL, ?, ?)", setting_name, setting_value)
    exec(setting_name + " = setting_value")
    return redirect("/settings")

#--------------------------------
@app.route("/log", methods=["GET", "POST"])
def log_page():
    input1 = request.form.get("name")
    if not input1:
        input1 = ""
    name = '%' + input1 + '%'
    input2 = request.form.get("datetime")
    if not input2:
        input2 = ""
    datetime = '%' + input2 + '%'
    log = db.execute("SELECT * FROM log LEFT JOIN people ON person_id = people.id WHERE (name LIKE ? OR datetime LIKE ?) AND (name LIKE ? OR datetime LIKE ?) ORDER BY datetime DESC",name, name, datetime, datetime)
    return render_template("/log.html", log=log)

@app.route("/log/search/<data>/")
def search_log(data):
    data1 = ""
    return render_template("/search_log.html", data=data, data1=data1)
#--------------------------------
@app.route("/people", methods=["GET", "POST"])
def people_page():
    input1 = request.form.get("name")
    if not input1:
        input1 = ""
    name = '%' + input1 + '%'
    people = db.execute("SELECT name, people.id, image_loc FROM people LEFT JOIN faces ON people.id=person_id WHERE name LIKE ? GROUP BY people.id ORDER BY name ASC", name)
    return render_template("/people.html", people=people)

@app.route("/people/search/<search>")
def search_people(search):
    return render_template("/search_people.html", name=search)
#--------------------------------
@app.route("/person/<person_id>")
def person_page(person_id):
    person = db.execute("SELECT * FROM people LEFT JOIN faces ON people.id=person_id WHERE people.id LIKE ? GROUP BY people.id", person_id)
    log = db.execute("SELECT * FROM log LEFT JOIN people ON person_id = people.id WHERE person_id LIKE ? OR datetime IN (SELECT datetime FROM log WHERE person_id LIKE ?) ORDER BY datetime DESC",person_id ,person_id)
    return render_template("/person.html", person=person, log=log)

@app.route("/person/delete", methods=["POST"])
def person_delete():
    del0 = request.form.get("del0")
    del1 = request.form.get("del1")
    del2 = request.form.get("del2")
    del3 = request.form.get("del3")
    del4 = request.form.get("del4")
    person_id = request.form.get("id")
    if del0 == del1 == del2 == del3 == del4 == True:
        faces = db.execute("SELECT image_loc FROM faces WHERE person_id=?", person_id)
        for image in faces:
            os.remove(image)
        db.execute("DELETE FROM faces WHERE person_id=?", person_id)
        db.execute("DELETE FROM people WHERE id=?", person_id)
        return redirect("/people.html/")
    return redirect("/person/" + str(person_id))

@app.route("/person/update", methods=["POST"])
def person_update():
    person_id = request.form.get("id")
    name = request.form.get("name")
    trusted = request.form.get("trusted")
    announce = request.form.get("announce")
    db.execute("UPDATE people SET name=?, trusted=?, announce=? WHERE id=?",name ,trusted ,announce ,person_id)
    return redirect("/person/" + str(person_id))
#--------------------------------

