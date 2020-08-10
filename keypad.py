from configs.matrixKeypad_RPi_GPIO import keypad
from configs.relay import *
from configs.camera import *
from time import sleep
from configs.config import db

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
while True:
    key = digit()
    print(key)
    if type(key) == int:
        code.append(key)
    elif key == "*" and len(code) >= 1:
        #code.pop()
        code = []
    elif key == "#":
        tocheck = arrtostr(code)
        print(tocheck)
        if tocheck in saved_pins_pin and saved_pins_trusted[saved_pins_pin.index(tocheck)] == 'True':
            print('ID', saved_pins_id[saved_pins_pin.index(tocheck)])
            if checkcamera(saved_pins_id[saved_pins_pin.index(tocheck)]):
                door_open(3)
            else:
                print('Cant see you')
            lockout = 0
        else:
            print('Pin not recognised')
            if len(code) >= 1:
                lockout += 1
            if lockout == 3:
                print('Lockout for 10 sec')
                sleep(10)
                lockout = 0
        tocheck = ''
        code = []
    #print(code)
    sleep(0.25)
