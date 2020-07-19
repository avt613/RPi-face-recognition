import face_recognition
from config import db
#query = db.execute("SELECT * FROM pictures WHERE path LIKE '%All/DCIM%' ORDER BY path ASC")
query = db.execute("SELECT * FROM pictures ORDER BY path ASC")
pictures = []
for i in range(len(query)):
    picid = query[i]["id"]
    image = query[i]["path"]
    print(image)
    #pictures.append(query[i]["path"])
    # Load an image with an unknown face
    unknown_image = face_recognition.load_image_file(image)
    # Find all the faces and face encodings in the unknown image
    face_locations = face_recognition.face_locations(unknown_image)
    if len(face_locations) == 0:
        db.execute("DELETE FROM pictures WHERE id=?",picid)
        print("removed from db")
    else:
        print("has at least 1 face")
