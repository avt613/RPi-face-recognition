gunicorn app:app -c configs/gunicorn.py --reload &
python3 camera.py &
python3 keypad.py &
