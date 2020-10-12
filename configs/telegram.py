from configs.config import telegramtoken, telegramid, telegramsilent, diagnostics
#--------telegram
import telepot
bot = telepot.Bot(telegramtoken)

from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

def telegram_send_button(title, text, link):
    markup = InlineKeyboardMarkup(inline_keyboard=[
                [dict(text=text, url=link)],
#                [InlineKeyboardButton(text='Callback - Done', callback_data='delete')],
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
