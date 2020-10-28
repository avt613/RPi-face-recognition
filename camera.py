import face_recognition
import picamera
import numpy as np
from configs.config import *
from configs.dbfunctions import *
from configs.telegram import *
from PIL import Image, ImageDraw
from datetime import timedelta, datetime
import uuid

camera = picamera.PiCamera()
camera.rotation = rotation
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

#---------- Reload faces
print("Loading known face image(s)")
res = dbget()
known_face_ids = res[0]
known_face_names = res[1]
#trusted = res[2]
#announce = res[3]
known_face_encoding = res[4]
known_face_locs = res[5]
tempname = ''
temptimestamp = ''

diag('camera.py: started')
#---------Proccess photo
def photoproc(face_locations, output):
    global tempname
    global temptimestamp
    face_encodings = face_recognition.face_encodings(output, face_locations)
    faces = Image.fromarray(output)
    temp = faces.save('static/temp.JPG')
    if televeryperson == 'True':
        telegram_send_photo('static/temp.JPG')
    # Loop over each face found in the frame to see if it's someone we know.
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        match = face_recognition.compare_faces(known_face_encoding, face_encoding, tolerance=float(tolerance))
        face_distances = face_recognition.face_distance(known_face_encoding, face_encoding)
        best_match_index = np.argmin(face_distances)
        if match[best_match_index]:
            name = known_face_names[best_match_index]
            person_id = known_face_ids[best_match_index]
            image_loc = known_face_locs[best_match_index]
        else:
            extrawidth = 0.2*(right - left)
            extraheight = 0.2*(bottom - top)
            face = faces.crop(((left - extrawidth), (top - 3*extraheight), (right + extrawidth), (bottom + extraheight)))
            image_loc = people_dir + str(uuid.uuid4()) + ".JPG"
            face.save(image_loc)
            face.close()
            person_id = db_person_add()
            name = "Unknown-" + str(person_id)
            db_face_add(person_id, image_loc, face_encoding)
            known_face_ids.append(person_id)
            known_face_names.append(name)
            #trusted.append(False)
            #announce.append()
            known_face_encoding.append(face_encoding)
            known_face_locs.append(image_loc)
        diag('camera.py: Person found: ' + str(person_id) + '; '+ name)

        #if same name within 9 seconds ignore
        timestamp = datetime.now()
        recent = set()
        for i in range(int(timedelay)):
            recent.add((datetime.now() - timedelta(seconds=i)))
        if not (temptimestamp in recent):
            if tempname != name and televeryperson == 'True':
                link = webaddress + ':' + str(webport) + '/person/' + str(person_id)
                telegram_send_button('ID: ' + str(person_id) + '\n' + 'NAME: ' + name, 'Open', link)
            db.execute('INSERT INTO log ("person_id", "datetime", "distance") VALUES(?, ?, ?)',person_id, timestamp, float(face_distances[best_match_index]))
        temptimestamp = timestamp
        tempname = name

        print(name, timestamp, float(face_distances[best_match_index]))


while True:
    camera.capture(output, format="rgb")
    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    if len(face_locations) >= 1:  
        photoproc(face_locations, output)
