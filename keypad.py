from configs.matrixKeypad_RPi_GPIO import keypad
from configs.relay import *
from configs.camera import *
from time import sleep
from configs.config import db
from configs.telegram import diag
from datetime import datetime

saved_pins_pin = []
saved_pins_id = []
saved_pins_trusted = []
query = db.execute("SELECT pin, id, trusted FROM people")
for i in range(len(query)):
    saved_pins_pin.append(query[i]['pin'])
    saved_pins_id.append(query[i]['id'])
    saved_pins_trusted.append(query[i]['trusted'])
    print(query[i]['id'], query[i]['pin'], query[i]['trusted'])
# Initialize the keypad class
kp = keypad()
 
def digit():
    # Loop while waiting for a keypress
    r = None
    while r == None:
        r = kp.getKey()
    return r 

def arrtostr(code):
    string = ''
    for i in range(len(code)):
        string += str(code[i])
    return string

print("Please enter your code: ")
 
# Getting digit 1, printing it, then sleep to allow the next digit press.
code = []
tocheck = ''
lockout = 0
#while len(code) <= 3:
diag('keypad.py: started')
while True:
    key = digit()
    print(key)
    if type(key) == int:
        code.append(key)
        diag('keypad.py: Key pressed:' + str(key))
    elif key == "*" and len(code) >= 1:
        #code.pop()
        code = []
        diag('keypad.py: Key pressed:' + str(key))
    elif key == "#":
        tocheck = arrtostr(code)
        print(tocheck)
        diag('keypad.py: Code entered:' + tocheck)
        if tocheck in saved_pins_pin and saved_pins_trusted[saved_pins_pin.index(tocheck)] == 'True':
            person_id = saved_pins_id[saved_pins_pin.index(tocheck)]
            print('ID', person_id)
            diag('keypad.py: Code of ID: ' + str( person_id))
            if checkcamera(person_id):
                diag('keypad.py: Door unlocked')
                door_open(3)
            else:
                print('Cant see you')
            lockout = 0
        else:
            person_id = 30
            print('Pin not recognised')
            if len(code) >= 1:
                lockout += 1
            if lockout == 3:
                diag('keypad.py: Lockout started')
                print('Lockout for 10 sec')
                sleep(10)
                diag('keypad.py: Lockout finnished')
                lockout = 0
        timestamp = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        db.execute('INSERT INTO log ("person_id", "datetime", "distance") VALUES(?, ?, ?)',person_id, timestamp, tocheck)
        tocheck = ''
        code = []
    #print(code)
    sleep(0.25)
