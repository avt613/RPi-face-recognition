from configs.matrixKeypad_RPi_GPIO import keypad
from configs.relay import *
from configs.camera import *
from time import sleep
from configs.config import db, masterpin, noneid
from configs.telegram import diag
from datetime import datetime
import RPi.GPIO as GPIO

saved_pins_pin = []
saved_pins_id = []
saved_pins_trusted = []
query = db.execute("SELECT pin, id FROM people WHERE (not  pin = '') and trusted = 'True'")
for i in range(len(query)):
    saved_pins_pin.append(query[i]['pin'])
    saved_pins_id.append(query[i]['id'])
    print(query[i]['id'], query[i]['pin'])
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
try:
    while True:
        key = digit()
        print(key)
        if type(key) == int:
            code.append(key)
            diag('keypad.py: Key pressed:' + str(key))
        elif key == "*" and len(code) >= 1:
            #code.pop() #remove last digit from code
            code = [] #reset code
            diag('keypad.py: Key pressed:' + str(key))
        elif key == "#":
            tocheck = arrtostr(code)
            print(tocheck)
            if (tocheck != ""):
                diag('keypad.py: Code entered:' + tocheck)
                person_id = int(noneid)
                if (tocheck == masterpin):
                    print("masterpin entered")
                    diag('keypad.py: Door unlocked, masterpin entered')
                    door_open(3)
                    lockout = 0
                elif (tocheck in saved_pins_pin):
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
finally:
    GPIO.cleanup()
