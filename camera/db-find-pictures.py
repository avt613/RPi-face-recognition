import face_recognition
from pathlib import Path
import glob
import os
from config import search, db, extentions
db.execute('DELETE FROM pictures')
for ext in extentions:
    images = glob.glob(search + '**/*.' + ext, recursive=True)
    for image in images:
        query = db.execute('INSERT INTO pictures VALUES(NULL, ?)',image)
        print(image)
        # Load an image with an unknown face
        #unknown_image = face_recognition.load_image_file(image)
        # Find all the faces and face encodings in the unknown image
        #face_locations = face_recognition.face_locations(unknown_image)
        #if len(face_locations) != 0:
            #filename = os.path.splitext(os.path.split(image)[1])[0]
            #print(image)
