# RPi face recognition
 Face recognising raspberry pi doorbell

This program is seperated into multiple sections, each controling a seperate part of the system. 
1) `app.py`    This is the web interface script. I run this with `gunicorn app:app -b 0.0.0.0`
2) `camera.py` This is the facial recognition script.
3) `live.py`   This controls the the live preview (This cannot be run at the same time as camera.py as only one script can use the camera at the same time)
4) `keypad.py` This controls the keypad (You can change the pins in `configs/matrixKeypad_RPi_GPIO.py`, line 31,32) 
To run this code, run the `run.sh` script.

## Instalation
