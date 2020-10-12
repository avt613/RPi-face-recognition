This project is still in progress. If you have any questions or comments please contact me.

# RPi face recognition
 Face recognizing raspberry pi doorbell

This program is seperated into multiple sections, each controling a seperate part of the system. 
1) `app.py`    This is the web interface script. I run this with `gunicorn app:app -b 0.0.0.0`
2) `camera.py` This is the facial recognition script.
3) `live.py`   This controls the the live preview (This cannot be run at the same time as camera.py as only one script can use the camera at the same time)
4) `keypad.py` This controls the keypad (You can change the pins in `configs/matrixKeypad_RPi_GPIO.py`, line 31,32) 

## Note
If you are not using a latching relay then you must change the configs/relay.py file.
This program uses the 'telepot' telegram library. If you do not want to use telegram then you will need to adjust the configs/telegram.py file


To run this code, run the `run.sh` script.

## Instalation
