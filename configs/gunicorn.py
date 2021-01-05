bind = '0.0.0.0:8000' 
workers = 2
from configs.config import db, webaddress, webport
from configs.telegram import telegram_send_button, telegram_send_text, on_telegram_message, telegram_send_keyboard, bot
#from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
#from telepot.loop import MessageLoop

def when_ready(server):
    telegram_send_button('Website Online', 'Open', webaddress + ':' + str(webport))
    #telegram_send_keyboard('Website Online', ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Unlock for 3 seconds")],[KeyboardButton(text="Unlock for 10 seconds")]]))
    #MessageLoop(bot, {'chat': on_telegram_message}).run_as_thread()
def on_exit(server):
    #telegram_send_keyboard('Website Offline', ReplyKeyboardRemove())
    telegram_send_text('Website Offline')
#preload_app = True
