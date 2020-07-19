from flask import Flask, flash, redirect, render_template, request, url_for
import random, os
import numpy as np
import face_recognition
from PIL import Image, ImageDraw
import uuid
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

#------------Import face encodings
# define an empty list
known_face_encodings = []
known_face_names = []

res = dbget()
known_face_encodings = res[0]
known_face_names = res[1]

#------------delete all saved images
if not os.path.exists(unknowndir):
    os.mkdir(unknowndir)
if not os.path.exists(knowndir):
    os.mkdir(knowndir)
filelist = [ f for f in os.listdir(unknowndir)]
for f in filelist:
    os.remove(os.path.join(unknowndir, f))

#--------------------------------

query = db.execute("SELECT * FROM pictures")
pictures = []
for i in range(len(query)):
    pictures.append([query[i]["id"],query[i]["path"]])
    

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/post", methods=["POST"])
def post():
    if request.method == "POST":
        length_pst = int(request.form.get("length"))
        known_face_encodings_toadd = []
        known_face_names_toadd = []
        known_face_images_toadd = []
        image_id_pst = request.form.get('picid')
        image_path_pst = request.form.get('picpath')
        os.remove('{0}{1}'.format(unknowndir, os.path.split(image_path_pst)[1]))
        for i in range(length_pst):
            picture = request.form.get('image_{0}_cut'.format(i))
            image_name_orig_pst = request.form.get('image_{0}_name_orig'.format(i))
            image_name_pst = request.form.get('image_{0}_name'.format(i))
            yn_pst = request.form.get('image_{0}_yn'.format(i))
            if image_name_orig_pst != image_name_pst and image_name_pst != "Unknown" and image_name_pst != "":
                face_image = face_recognition.load_image_file(unknowndir + picture)
                face_face_encoding = face_recognition.face_encodings(face_image)[0]
                known_face_encodings_toadd.append(face_face_encoding)
                known_face_names_toadd.append(image_name_pst)
                known_face_encodings.append(face_face_encoding)
                known_face_names.append(image_name_pst)
                newimageloc = knowndir + image_name_pst + "-" + str(uuid.uuid1()) + ".JPG"
                known_face_images_toadd.append(newimageloc)
                os.rename(unknowndir + picture, newimageloc)
            else:
                os.remove(unknowndir + picture) 
        dbadd(known_face_encodings_toadd, known_face_names_toadd, known_face_images_toadd)
    return redirect("pic")

@app.route("/pic")
def pic():
    random_picture = random.choice(pictures)
    random_picid = random_picture[0]
    #while random_picid == image_id_pst:
    #    random_picture = random.choice(pictures)
    #    random_picid = random_picture[0]
    random_filename = random_picture[1]
    length = ""
    cut_faces = cut(random_filename)
    length = len(cut_faces)
    return render_template("pic.html", random=os.path.split(random_filename)[1], picid=random_picid, picpath=random_filename, cut_faces=cut_faces, length=length)

#------------Extract faces
def cut(imagename):
    cut_faces = []
    # Load an image with an unknown face
    unknown_image = face_recognition.load_image_file(imagename)
    # Find all the faces and face encodings in the unknown image
    face_locations = face_recognition.face_locations(unknown_image, number_of_times_to_upsample=2)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
    # Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
    # See http://pillow.readthedocs.io/ for more about PIL/Pillow
    pil_image = Image.fromarray(unknown_image)
    faces = Image.open(imagename)
    # Create a Pillow ImageDraw Draw instance to draw with
    draw = ImageDraw.Draw(pil_image)
    facenum = 0
    # Loop through each face found in the unknown image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=tolerance)
        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        else:
            name = "Unknown"
        extrawidth = 0.2*(right - left)
        extraheight = 0.2*(bottom - top)
        face = faces.crop(((left - extrawidth), (top - 3*extraheight), (right + extrawidth), (bottom + extraheight)))
        unique = uuid.uuid1()
        face.save('{0}{1}-{2}.JPG'.format(unknowndir, facenum, unique))
        face.close()
        cut_faces.append(['{0}-{1}.JPG'.format(facenum, unique), name, facenum])
        facenum += 1
        if name != "none":
            # Draw a box around the face using the Pillow module
            draw.rectangle(((left, top), (right, bottom)), outline=(255, 0, 0), width=5)
    # Display the resulting image
    pil_image.save('{0}{1}'.format(unknowndir, os.path.split(imagename)[1]))
    return cut_faces
