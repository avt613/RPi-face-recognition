from config import *
import sys
import time
import threading
import random
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent

message_with_inline_keyboard = None

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)

    if content_type != 'text':
        return

    command = msg['text'][-1:].lower()

    if command == 'help':
        markup = InlineKeyboardMarkup(inline_keyboard=[
                     [dict(text='Homepage', url=webaddress)],
                     [InlineKeyboardButton(text='Callback - edit message', callback_data='edit')],
                     [InlineKeyboardButton(text='Callback - delete message', callback_data='delete')],
                     [dict(text='Switch to using bot inline', switch_inline_query='initial query')],
                 ])

        global message_with_inline_keyboard
        message_with_inline_keyboard = bot.sendMessage(chat_id, 'Inline keyboard with various buttons', reply_markup=markup)
        print(message_with_inline_keyboard)

def on_callback_query(msg):
    query_id, from_id, data = telepot.glance(msg, flavor='callback_query')
    print('Callback query:', query_id, from_id, data)

    if data == 'notification':
        bot.answerCallbackQuery(query_id, text='Notification at top of screen')
    elif data == 'alert':
        bot.answerCallbackQuery(query_id, text='Alert!', show_alert=True)
    elif data == 'edit':
        global message_with_inline_keyboard

        if message_with_inline_keyboard:
            msg_idf = telepot.message_identifier(message_with_inline_keyboard)
            bot.editMessageText(msg_idf, 'NEW MESSAGE HERE!!!!!')
        else:
            bot.answerCallbackQuery(query_id, text='No previous message to edit')
    elif data == 'delete':
        global telegram_message
        if message_with_inline_keyboard:
            msg_idf = telepot.message_identifier(message_with_inline_keyboard)
            print(msg_idf)
            bot.deleteMessage(msg_idf)


def on_inline_query(msg):
    def compute():
        query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
        print('%s: Computing for: %s' % (threading.current_thread().name, query_string))

        articles = [InlineQueryResultArticle(
                        id='abcde', title='Telegram', input_message_content=InputTextMessageContent(message_text='Telegram is a messaging app')),
                    dict(type='article',
                        id='fghij', title='Google', input_message_content=dict(message_text='Google is a search engine'))]

        photo1_url = 'https://core.telegram.org/file/811140934/1/tbDSLHSaijc/fdcc7b6d5fb3354adf'
        photo2_url = 'https://www.telegram.org/img/t_logo.png'
        photos = [InlineQueryResultPhoto(
                      id='12345', photo_url=photo1_url, thumb_url=photo1_url),
                  dict(type='photo',
                      id='67890', photo_url=photo2_url, thumb_url=photo2_url)]

        result_type = query_string[-1:].lower()

        if result_type == 'a':
            return articles
        elif result_type == 'p':
            return photos
        else:
            results = articles if random.randint(0,1) else photos
            if result_type == 'b':
                return dict(results=results, switch_pm_text='Back to Bot', switch_pm_parameter='Optional_start_parameter')
            else:
                return dict(results=results)

    answerer.answer(msg, compute)


def on_chosen_inline_result(msg):
    result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
    print('Chosen Inline Result:', result_id, from_id, query_string)


answerer = telepot.helper.Answerer(bot)

MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query,
                  'inline_query': on_inline_query,
                  'chosen_inline_result': on_chosen_inline_result}).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)