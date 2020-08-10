sudo cp camera.service /etc/systemd/system/camera.service
sudo systemctl enable camera.service
sudo systemctl start camera.service

sudo cp gunicorn.service /etc/systemd/system/gunicorn.service
sudo systemctl enable gunicorn.service
sudo systemctl start gunicorn.service

sudo cp keypad.service /etc/systemd/system/keypad.service
sudo systemctl enable keypad.service
sudo systemctl start keypad.service

sudo cp live.service /etc/systemd/system/live.service
