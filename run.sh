gunicorn app:app -b 0.0.0.0 --reload &
python3 camera.py
