import datetime
import logging

import config
import datetime
import telebot
from telebot import apihelper, types
import sqlite3
import inline_calendar

import telebot
from telebot import types
import inline_calendar

apihelper.proxy = {'http':'http://10.10.1.10:3128'}

YOUR_TOKEN = '****'
bot = telebot.TeleBot(token=YOUR_TOKEN)


@bot.message_handler(commands=['calendar'])
def calendar_test(message):
    inline_calendar.init(message.from_user.id,
                         datetime.date.today(),
                         datetime.date(year=2019, month=1, day=1),
                         datetime.date(year=2020, month=12, day=31))
    bot.send_message(message.from_user.id, text='test', reply_markup=inline_calendar.get_keyboard(message.from_user.id))


@bot.callback_query_handler(func=lambda call: True)#func=inline_calendar.is_inline_calendar_callbackquery)
def calendar_callback_handler(call):
    print(call)
    bot.answer_callback_query(call.id)
    #print(bot.answer_callback_query(q.id))
    #print(q.id)
    print(call.data)
    try:
        return_data = inline_calendar.handler_callback(call.from_user.id, call.data)
        print(return_data)
        print(call.from_user.id)
        if return_data is None:
            bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,
                                          reply_markup=inline_calendar.get_keyboard(call.from_user.id))
        else:
            picked_data = return_data
            bot.send_message(text= "Вы записанны. Ваша дата записи:", chat_id=call.from_user.id)
            bot.send_message(text=picked_data, chat_id=call.from_user.id)

    except inline_calendar.WrongChoiceCallbackException:
        bot.edit_message_text(text='Ошибка', chat_id=call.from_user.id, message_id=call.message.message_id,
                              reply_markup=inline_calendar.get_keyboard(call.from_user.id))


if __name__ == '__main__':
    bot.polling(none_stop=True)

