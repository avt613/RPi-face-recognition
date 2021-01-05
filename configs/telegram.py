from configs.config import telegramtoken, telegramid, telegramsilent, diagnostics
#--------telegram
import telepot
bot = telepot.Bot(telegramtoken)

from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
try:
    from configs.relay import *
except:
    server.log.info("No module named 'RPi'")
import sys
import time
#from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
    
def telegram_send_keyboard(title, markup):
    global telegram_message
    telegram_message = bot.sendMessage(telegramid, title, reply_markup=markup, disable_notification=telegramsilent)
    
def telegram_send_button(title, text, link):
    markup = InlineKeyboardMarkup(inline_keyboard=[
                [dict(text=text, url=link)]
             ])
    global telegram_message
    telegram_message = bot.sendMessage(telegramid, title, reply_markup=markup, disable_notification=telegramsilent)

def telegram_send_photobutton(text, link, image_loc):
    markup = InlineKeyboardMarkup(inline_keyboard=[
                [dict(text=text, url=link)],
             ])
    global telegram_message
    telegram_message = bot.sendPhoto(telegramid, photo=open(image_loc, 'rb'), reply_markup=markup, disable_notification=telegramsilent)

def telegram_send_photo(image_loc):
    bot.sendPhoto(telegramid, photo=open(image_loc, 'rb'), disable_notification=telegramsilent)

def telegram_send_text(text):
    bot.sendMessage(telegramid, text, disable_notification=telegramsilent)

def diag(text):
    if(diagnostics == 'True'):
        bot.sendMessage(telegramid, 'DIAG: ' + text, disable_notification=telegramsilent)

def on_telegram_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat Message:', content_type, chat_type, chat_id, telegramid)

    if (content_type == 'text'):
        print('the taxt was' ,msg['text'])
        #if msg['text'] == '/key':
        #    bot.sendMessage(chat_id, 'Loading Keyboard', reply_markup=(unlockKeyboard)
        #elif msg['text'] == 'Close Keyboard':
        #    bot.deleteMessage(telepot.message_identifier(msg))
        #    bot.deleteMessage(telepot.message_identifier(bot.sendMessage(chat_id, 'Deleting keyboard', reply_markup=ReplyKeyboardRemove())))
        if msg['text'] == 'Unlock for 3 seconds':
            print("Unlock for 3 seconds")
            door_open(3)
        elif msg['text'] == 'Unlock for 10 seconds':
            door_open(10)
