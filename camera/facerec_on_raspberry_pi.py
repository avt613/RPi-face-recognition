# This is a demo of running face recognition on a Raspberry Pi.
# This program will print out the names of anyone it recognizes to the console.

# To run this, you need a Raspberry Pi 2 (or greater) with face_recognition and
# the picamera[array] module installed.
# You can follow this installation instructions to get your RPi set up:
# https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65

import face_recognition
import picamera
import numpy as np
from config import *
from datetime import datetime
from PIL import Image, ImageDraw
import uuid

# Get a reference to the Raspberry Pi camera.
# If this fails, make sure you have a camera connected to the RPi and that you
# enabled your camera in raspi-config and rebooted first.
camera = picamera.PiCamera()
camera.rotation = 180
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

# Load a sample picture and learn how to recognize it.
print("Loading known face image(s)")
#obama_image = face_recognition.load_image_file("obama_small.jpg")
#obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Initialize some variables
face_locations = []
face_encodings = []

res = dbget()
known_face_encoding = res[0]
known_person = res[1]


while True:
    #print("Capturing image.")
    # Grab a single frame of video from the RPi camera as a numpy array
    camera.capture(output, format="rgb")
    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)

    i = 0
    #faces = face_recognition.load_image_file(output)
    faces = Image.fromarray(output)
    #faces = Image.open(pil_image)

    # Loop over each face found in the frame to see if it's someone we know.
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces(known_face_encoding, face_encoding, tolerance=tolerance)
        name = "<Unknown Person>"

        face_distances = face_recognition.face_distance(known_face_encoding, face_encoding)
        best_match_index = np.argmin(face_distances)
        if match[best_match_index]:
            name = known_person[best_match_index]
        else:
            name = "Unknown"
            extrawidth = 0.2*(right - left)
            extraheight = 0.2*(bottom - top)
            face = faces.crop(((left - extrawidth), (top - 3*extraheight), (right + extrawidth), (bottom + extraheight)))
            unique = uuid.uuid1()
            face.save('{0}{1}.JPG'.format(search, unique))
            face.close()
            db.execute('INSERT INTO pictures VALUES(NULL, ?)',(search + str(unique) + '.JPG'))
        timestamp = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        db.execute('INSERT INTO log ("name", "datetime", "distance") VALUES(?, ?, ?)',name, timestamp, float(face_distances[best_match_index]))
        print(name, timestamp, float(face_distances[best_match_index]))
        i =+ 1
