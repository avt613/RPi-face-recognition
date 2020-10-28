from flask import Flask, flash, redirect, render_template, request, url_for
from configs.services import *
from configs.config import db, webaddress, webport
import os
try:
    from configs.relay import *
except:
    server.log.info("No module named 'RPi'")

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
    return redirect("/log")

@app.route("/unlock")
def unlock():
    door_open(3)
    return redirect("/")

#--------------------------------
@app.route("/settings")
def settings_page():
    settings = db.execute("SELECT * FROM settings ORDER BY name ASC")
    service_status = []
    for i in range(len(services_list)):
        if service_active(services_list[i]):
            service_status.append('Active')
        else:
            service_status.append('NOT Active')
    return render_template("/settings.html", settings=settings, services_list=services_list, service_status=service_status)

@app.route("/settings/update", methods=["POST"])
def settings_update():
    setting_id = request.form.get("id")
    setting_name = request.form.get("name")
    setting_value = request.form.get("value")
    setting_notes = request.form.get("notes")
    settings = db.execute("UPDATE settings SET name=?, value=?, notes=? WHERE id=?", setting_name, setting_value, setting_notes, setting_id)
    exec(setting_name + " = setting_value")
    return redirect("/settings")

@app.route("/settings/delete", methods=["POST"])
def settings_delete():
    setting_id = request.form.get("id")
    setting_name = request.form.get("name")
    settings = db.execute("DELETE FROM settings WHERE id=?", setting_id)
    return redirect("/settings")

@app.route("/settings/new", methods=["POST"])
def settings_new():
    setting_name = request.form.get("name")
    setting_value = request.form.get("value")
    setting_notes = request.form.get("notes")
    settings = db.execute("INSERT INTO settings VALUES(NULL, ?, ?, ?)", setting_name, setting_value, setting_notes)
    exec(setting_name + " = setting_value")
    return redirect("/settings")

@app.route("/settings/restart/<service>", methods=["POST"])
def settings_restart(service):
    if service == 'pi':
        os.system("sudo reboot now")
    elif service == 'all':
    
        for service in services_list.pop(services_list.index('live')):
            restart_service(service)
        services_list.append('live')
    else:
        if service == 'camera':
            stop_service('live')
        elif service == 'live':
            stop_service('camera')
        restart_service(service)
    return redirect("/settings")

@app.route("/settings/halt_pi", methods=["POST"])
def settings_halt_pi():
    os.system("sudo halt")
    return redirect("/settings")

@app.route("/settings/stop/<service>", methods=["POST"])
def settings_stop(service):
    if service == 'pi':
        os.system("sudo halt")
    else:
        stop_service(service)
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
    log = db.execute("SELECT * FROM log JOIN people ON person_id = people.id WHERE (name LIKE ? OR datetime LIKE ?) AND (name LIKE ? OR datetime LIKE ?) ORDER BY datetime DESC",name, name, datetime, datetime)
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
    if name == "%unknown%":
        people = db.execute("SELECT name, people.id, image_loc FROM people LEFT JOIN faces ON people.id=person_id WHERE name LIKE 'unknown%' GROUP BY people.id ORDER BY people.id DESC")
    else:
        people = db.execute("SELECT name, people.id, image_loc FROM people LEFT JOIN faces ON people.id=person_id WHERE name LIKE ? AND name NOT LIKE 'unknown%' GROUP BY people.id ORDER BY name", name)
    return render_template("/people.html", people=people)

@app.route("/people/search/<search>")
def search_people(search):
    return render_template("/search_people.html", name=search)
#--------------------------------
@app.route("/person/<person_id>")
def person_page(person_id):
    person = db.execute("select * from people join faces on people.id = faces.person_id where people.id = ?", person_id)
    log = db.execute("SELECT * FROM log JOIN people ON person_id = people.id WHERE person_id LIKE ? OR datetime IN (SELECT datetime FROM log WHERE person_id LIKE ?) ORDER BY datetime DESC",person_id ,person_id)
    return render_template("/person.html", person=person, log=log)

@app.route("/person/delete", methods=["POST"])
def person_delete():
    del0 = request.form.get("del0")
    del1 = request.form.get("del1")
    del2 = request.form.get("del2")
    del3 = request.form.get("del3")
    del4 = request.form.get("del4")
    person_id = request.form.get("id")
    if del0 == del1 == del2 == del3 == del4 == 'True':
        faces = db.execute("SELECT image_loc FROM faces WHERE person_id=?", person_id)
        for i in range(len(faces)):
            os.remove(faces[i]['image_loc'])
        db.execute("DELETE FROM faces WHERE person_id=?", int(person_id))
        db.execute("DELETE FROM log WHERE person_id=?", int(person_id))
        db.execute("DELETE FROM people WHERE id=?", int(person_id))
        return redirect("/people")
    return redirect("/person/" + str(person_id))

@app.route("/person/deleteface", methods=["POST"])
def person_delete_face():
    person_id = request.form.get("id")
    face = request.form.get("face")
    faces = db.execute("SELECT count(image_loc) AS count FROM faces WHERE person_id=?", person_id)
    if faces[0]['count'] > 1:
        os.remove(face)
        db.execute("DELETE FROM faces WHERE image_loc=?", face)
    return redirect("/person/" + str(person_id))

@app.route("/person/update", methods=["POST"])
def person_update():
    person_id = request.form.get("id")
    name = request.form.get("name")
    trusted = str(request.form.get("trusted"))
    announce = request.form.get("announce")
    pin = request.form.get("pin")
    db.execute("UPDATE people SET name=?, trusted=?, announce=?, pin=? WHERE id=?",name ,trusted ,announce, pin ,person_id)
    return redirect("/person/" + str(person_id))

@app.route("/person/addto", methods=["POST"])
def person_addto():
    person_id = request.form.get("id")
    addtoid = request.form.get("addtoid")
    db.execute("UPDATE faces SET person_id=? WHERE person_id=?", addtoid, person_id)
    db.execute("UPDATE log SET person_id=? WHERE person_id=?", addtoid, person_id)
    db.execute("DELETE FROM people WHERE id=?", person_id)
    return redirect("/person/" + str(addtoid))

@app.route("/person/fix", methods=["POST"])
def person_fix():
    person_id = request.form.get("id")
    db.execute("INSERT INTO log (person_id) VALUES(?)", int(person_id))
    return redirect("/person/" + str(person_id))
#--------------------------------

