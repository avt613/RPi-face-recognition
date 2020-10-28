bind = '0.0.0.0:8000' 
workers = 2
from configs.config import db, webaddress, webport
from configs.telegram import telegram_send_button, telegram_send_text

def when_ready(server):
    telegram_send_button('Website Online', 'Open', webaddress + ':' + str(webport))   
def on_exit(server):
    telegram_send_text('Website Offline')
#preload_app = True

