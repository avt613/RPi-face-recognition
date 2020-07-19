# Image-Face-Recognition
Using face recognition to identify people in photos

you can download this and run it with "gunicorn app:app"

config.py - contains most of the configurations used in the other scripts.

db-count-pictures.py - outputs the number of images in the db

db-find-pictures.py - adds all images to the db from a specific folder (includes subfolders). (Deletes previously added ones) Images need to be in the db in order for the program to display them. You may want to run "db-remove-empty.py" after running this. Note: the program doesn't seem to like "PNG"s 

db-remove-empty.py - looks through all photos in the db and removes pictures which do not contain any faces from the db

requirements.txt - all python requirements for this program

data/faces.db - database containing faces (names and encodings) and location of all pictures. Note: there must always be at least one face encoding in the db for the program to work.

static/all/ - place to put pictures

static/assets/img/ - temporary location for images when page loaded (MUST EXIST)
