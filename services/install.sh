sudo cp camera.service /etc/systemd/system
sudo systemctl enable camera.service
sudo systemctl start camera.service
sudo cp gunicorn.service /etc/systemd/system
sudo systemctl enable gunicorn.service
sudo systemctl start gunicorn.service
sudo cp live.service /etc/systemd/system
