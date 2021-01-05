from configs.config import *
import os
import base64

for file in os.listdir(people_dir):
    if file.endswith(".JPG"):
        print(os.path.join(people_dir, file))
        with open(os.path.join(people_dir, file), "rb") as img_file:
            my_string = base64.b64encode(img_file.read())
        print("data:image/png;base64," + my_string.decode('utf-8'))
        query = db.execute("UPDATE faces SET image_loc='data:image/png;base64," + my_string.decode('utf-8') + "' WHERE image_loc='"+ os.path.join(people_dir, file) +"'")
        os.remove(os.path.join(people_dir, file))
