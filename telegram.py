from configs.config import telegramtoken, telegramid, telegramsilent

import sys
import time
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
unlockKeyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Unlock for 3 seconds")], 
            [KeyboardButton(text="Unlock for 10 seconds")] 
            #,[KeyboardButton(text="Close Keyboard")]
        ]
    )

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat Message:', content_type, chat_type, chat_id)

    if content_type == 'text' && chat_id == telegramid:
        #if msg['text'] == '/key':
        #    bot.sendMessage(chat_id, 'Loading Keyboard', reply_markup=(unlockKeyboard)
        #elif msg['text'] == 'Close Keyboard':
        #    bot.deleteMessage(telepot.message_identifier(msg))
        #    bot.deleteMessage(telepot.message_identifier(bot.sendMessage(chat_id, 'Deleting keyboard', reply_markup=ReplyKeyboardRemove())))
        if msg['text'] == 'Unlock for 3 seconds':
            door_open(3)
        elif msg['text'] == 'Unlock for 10 seconds':
            door_open(10)
            

bot = telepot.Bot(telegramtoken)
print('Listening ...')
bot.message_loop({'chat': on_chat_message}, run_forever=True)
