# -*- coding: utf-8 -*-
import config
import datetime
import telebot

from telebot import apihelper, types
import sqlite3
import inline_calendar

apihelper.proxy = {'http':'http://10.10.1.10:3128'}

token = '668604627:AAEXYzo_Ge_eZ5pcdm6zPsJwcmc5cnu_yl8'
bot = telebot.TeleBot(token, threaded=False)





@bot.message_handler(commands=["start"])
def default_test(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('Старт')
    msg = bot.send_message(message.chat.id,text='Здравствуйте! Я онлайн-помощник компании «Аудэкс» - крупнейшей региональной аудиторско-консалтинговой компании России. Мы помогаем бизнесу принимать правильные решения уже 25 лет. Здесь Вы можете записаться на консультацию или узнать подробнее об услугах компании. Нажмите Старт.',reply_markup=keyboard)
    bot.register_next_step_handler(msg, menu)

@bot.message_handler(func=lambda message: message.text == "Старт")
def menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Аудит','Налоговый консалтинг','Юридические услуги','Бухгалтерские услуги','Оценка')
    keyboard.add('Обучение', 'Автоматизация бизнеса', 'Нужна консультация', 'Сайт', 'Контакты')
    msg = bot.send_message(message.chat.id, 'Какая услуга Вас интересует?', reply_markup=keyboard)
    bot.register_next_step_handler(msg, main_menu)


@bot.message_handler(func=lambda message: message.text == "/назад")
def back_menu(message):
    msg = bot.send_message(message.chat.id, '/назад')
    bot.register_next_step_handler(msg, menu)

@bot.message_handler()
def site_back_1(message): #1
    if message.text == 'Сайт компании':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru', reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)
    #elif message.text == 'Назад':
    #    msg = bot.send_message(message.chat.id,'/назад')
    #    bot.register_next_step_handler(msg, menu)#Два клика/исправить
    if message.text == "Подробнее":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru/services/auditorskie-uslugi/',reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)

@bot.message_handler()
def site_back_2(message): #2
    if message.text == 'Сайт компании':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru', reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)
    #elif message.text == 'Назад':
    #    msg = bot.send_message(message.chat.id,'/назад')
    #    bot.register_next_step_handler(msg, menu)#Два клика/исправить
    if message.text == "Подробнее":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, ' https://audex.ru/services/nalogovyy-i-bukhgalterskiy-konsalting/',reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)

@bot.message_handler()
def site_back_3(message): #3
    if message.text == 'Сайт компании':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru', reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)
    elif message.text == 'Назад':
        msg = bot.send_message(message.chat.id,'/назад')
        bot.register_next_step_handler(msg, menu)#Два клика/исправить
    if message.text == "Подробнее":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru/services/yuridicheskiy-konsalting/',reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)

@bot.message_handler()
def site_back_4(message): #4
    if message.text == 'Сайт компании':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru', reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)
    elif message.text == 'Назад':
        msg = bot.send_message(message.chat.id,'/назад')
        bot.register_next_step_handler(msg, menu)#Два клика/исправить
    if message.text == "Подробнее":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru/services/vedenie-bukhgalterskogo-ucheta/',reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)

@bot.message_handler()
def site_back_5(message): #5
    if message.text == 'Сайт компании':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru', reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)
    elif message.text == 'Назад':
        msg = bot.send_message(message.chat.id,'/назад')
        bot.register_next_step_handler(msg, menu)#Два клика/исправить
    if message.text == "Подробнее":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru/services/otsenka/',reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)

@bot.message_handler()
def site_back_6(message): #6
    if message.text == 'Сайт компании':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru', reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)
    elif message.text == 'Назад':
        msg = bot.send_message(message.chat.id,'/назад')
        bot.register_next_step_handler(msg, menu)#Два клика/исправить
    if message.text == "Подробнее":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru/services/obuchenie/',reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)

@bot.message_handler()
def site_back_7(message): #7
    if message.text == 'Сайт компании':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru', reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)
    elif message.text == 'Назад':
        msg = bot.send_message(message.chat.id,'/назад')
        bot.register_next_step_handler(msg, menu)#Два клика/исправить
    if message.text == "Подробнее":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru/services/it-konsalting/',reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)

@bot.message_handler()
def site_back_8(message): #8
    if message.text == 'Сайт компании':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru', reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)
    elif message.text == 'Назад':
        msg = bot.send_message(message.chat.id,'/назад')
        bot.register_next_step_handler(msg, menu)#Два клика/исправить
    if message.text == "Подробнее":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru/services/it-konsalting/',reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)

@bot.message_handler()
def sps(message): #1
    """
    Процесс клика на кнопки "Прислать контакт"
    """
    #if message.text == pris_kont.text:
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('Сайт компании')
    keyboard.add('Подробнее')
    keyboard.add('/назад')
    msg = bot.send_message(message.chat.id,
                         'Спасибо, наши менеджеры свяжутся с Вами в ближайшее время!', reply_markup=keyboard)

    ################## DATABASE #######################
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    phone = message.contact.phone_number
    names = message.contact.first_name
    zakaz = 'Аудит'
    try:
        c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, phone VARCHAR, names VARCHAR, zakaz VARCHAR)''')
    except:
        print('--------------')

    def add_phone(userphone, f_names, order):
        c.execute(
            "INSERT INTO users(phone, names, zakaz)  VALUES ('{0}', '{1}', '{2}')".format(userphone, f_names, order))
        conn.commit()

    add_phone(phone, names, zakaz)
    c.execute('SELECT * FROM users')
    row = c.fetchone()
    while row is not None:
        print("id: " + str(row[0]) + " Phone: " + str(row[1]) + " Name: " + row[2] + " Call: " + row[3])
        row = c.fetchone()
    c.close()
    conn.close()
    ################## DATABASE #######################

    bot.register_next_step_handler(msg, site_back_1)

@bot.message_handler()
def sps2(message): #2
    """
    Процесс клика на кнопки "Прислать контакт"
    """
    #if message.text == pris_kont.text:
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('Сайт компании')
    keyboard.add('Подробнее')
    keyboard.add('/назад')
    msg = bot.send_message(message.chat.id,
                         'Спасибо, наши менеджеры свяжутся с Вами в ближайшее время!', reply_markup=keyboard)

    ################## DATABASE #######################
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    phone = message.contact.phone_number
    names = message.contact.first_name
    zakaz = 'Налоговый консалтинг'
    try:
        c.execute(
            '''CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, phone VARCHAR, names VARCHAR, zakaz VARCHAR)''')
    except:
        print('--------------')

    def add_phone(userphone, f_names, order):
        c.execute(
            "INSERT INTO users(phone, names, zakaz)  VALUES ('{0}', '{1}', '{2}')".format(userphone, f_names, order))
        conn.commit()

    add_phone(phone, names, zakaz)
    c.execute('SELECT * FROM users')
    row = c.fetchone()
    while row is not None:
        print("id: " + str(row[0]) + " Phone: " + str(row[1]) + " Name: " + row[2] + " Call: " + row[3])
        row = c.fetchone()
    c.close()
    conn.close()
    ################## DATABASE #######################

    bot.register_next_step_handler(msg, site_back_2)

@bot.message_handler()
def sps3(message): #3
    """
    Процесс клика на кнопки "Прислать контакт"
    """
    #if message.text == pris_kont.text:
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('Сайт компании')
    keyboard.add('Подробнее')
    keyboard.add('/назад')
    msg = bot.send_message(message.chat.id,
                         'Спасибо, наши менеджеры свяжутся с Вами в ближайшее время!', reply_markup=keyboard)

    ################## DATABASE #######################
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    phone = message.contact.phone_number
    names = message.contact.first_name
    zakaz = 'Юридические услуги'
    try:
        c.execute(
            '''CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, phone VARCHAR, names VARCHAR, zakaz VARCHAR)''')
    except:
        print('--------------')

    def add_phone(userphone, f_names, order):
        c.execute(
            "INSERT INTO users(phone, names, zakaz)  VALUES ('{0}', '{1}', '{2}')".format(userphone, f_names, order))
        conn.commit()

    add_phone(phone, names, zakaz)
    c.execute('SELECT * FROM users')
    row = c.fetchone()
    while row is not None:
        print("id: " + str(row[0]) + " Phone: " + str(row[1]) + " Name: " + row[2] + " Call: " + row[3])
        row = c.fetchone()
    c.close()
    conn.close()
    ################## DATABASE #######################

    bot.register_next_step_handler(msg, site_back_3)

@bot.message_handler()
def sps4(message): #4
    """
    Процесс клика на кнопки "Прислать контакт"
    """
    #if message.text == pris_kont.text:
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('Сайт компании')
    keyboard.add('Подробнее')
    keyboard.add('/назад')
    msg = bot.send_message(message.chat.id,
                         'Спасибо, наши менеджеры свяжутся с Вами в ближайшее время!', reply_markup=keyboard)

    ################## DATABASE #######################
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    phone = message.contact.phone_number
    names = message.contact.first_name
    zakaz = 'Бухгалтерские услуги'
    try:
        c.execute(
            '''CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, phone VARCHAR, names VARCHAR, zakaz VARCHAR)''')
    except:
        print('--------------')

    def add_phone(userphone, f_names, order):
        c.execute(
            "INSERT INTO users(phone, names, zakaz)  VALUES ('{0}', '{1}', '{2}')".format(userphone, f_names, order))
        conn.commit()

    add_phone(phone, names, zakaz)
    c.execute('SELECT * FROM users')
    row = c.fetchone()
    while row is not None:
        print("id: " + str(row[0]) + " Phone: " + str(row[1]) + " Name: " + row[2] + " Call: " + row[3])
        row = c.fetchone()
    c.close()
    conn.close()
    ################## DATABASE #######################

    bot.register_next_step_handler(msg, site_back_4)

@bot.message_handler()
def sps5(message): #5
    """
    Процесс клика на кнопки "Прислать контакт"
    """
    #if message.text == pris_kont.text:
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('Сайт компании')
    keyboard.add('Подробнее')
    keyboard.add('/назад')
    msg = bot.send_message(message.chat.id,
                         'Спасибо, наши менеджеры свяжутся с Вами в ближайшее время!', reply_markup=keyboard)

    ################## DATABASE #######################
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    phone = message.contact.phone_number
    names = message.contact.first_name
    zakaz = 'Оценка'
    try:
        c.execute(
            '''CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, phone VARCHAR, names VARCHAR, zakaz VARCHAR)''')
    except:
        print('--------------')

    def add_phone(userphone, f_names, order):
        c.execute(
            "INSERT INTO users(phone, names, zakaz)  VALUES ('{0}', '{1}', '{2}')".format(userphone, f_names, order))
        conn.commit()

    add_phone(phone, names, zakaz)
    c.execute('SELECT * FROM users')
    row = c.fetchone()
    while row is not None:
        print("id: " + str(row[0]) + " Phone: " + str(row[1]) + " Name: " + row[2] + " Call: " + row[3])
        row = c.fetchone()
    c.close()
    conn.close()
    ################## DATABASE #######################

    bot.register_next_step_handler(msg, site_back_5)

@bot.message_handler()
def sps6(message): #6
    """
    Процесс клика на кнопки "Прислать контакт"
    """
    #if message.text == pris_kont.text:
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('Сайт компании')
    keyboard.add('Подробнее')
    keyboard.add('/назад')
    msg = bot.send_message(message.chat.id,
                         'Спасибо, наши менеджеры свяжутся с Вами в ближайшее время!', reply_markup=keyboard)

    ################## DATABASE #######################
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    phone = message.contact.phone_number
    names = message.contact.first_name
    zakaz = 'Обучение'
    try:
        c.execute(
            '''CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, phone VARCHAR, names VARCHAR, zakaz VARCHAR)''')
    except:
        print('--------------')

    def add_phone(userphone, f_names, order):
        c.execute(
            "INSERT INTO users(phone, names, zakaz)  VALUES ('{0}', '{1}', '{2}')".format(userphone, f_names, order))
        conn.commit()

    add_phone(phone, names, zakaz)
    c.execute('SELECT * FROM users')
    row = c.fetchone()
    while row is not None:
        print("id: " + str(row[0]) + " Phone: " + str(row[1]) + " Name: " + row[2] + " Call: " + row[3])
        row = c.fetchone()
    c.close()
    conn.close()
    ################## DATABASE #######################

    bot.register_next_step_handler(msg, site_back_6)

@bot.message_handler()
def sps7(message): #7
    """
    Процесс клика на кнопки "Прислать контакт"
    """
    #if message.text == pris_kont.text:
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('Сайт компании')
    keyboard.add('Подробнее')
    keyboard.add('/назад')
    msg = bot.send_message(message.chat.id,
                         'Спасибо, наши менеджеры свяжутся с Вами в ближайшее время!', reply_markup=keyboard)

    ################## DATABASE #######################
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    phone = message.contact.phone_number
    names = message.contact.first_name
    zakaz = 'Автоматизация бизнеса'
    try:
        c.execute(
            '''CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, phone VARCHAR, names VARCHAR, zakaz VARCHAR)''')
    except:
        print('--------------')

    def add_phone(userphone, f_names, order):
        c.execute(
            "INSERT INTO users(phone, names, zakaz)  VALUES ('{0}', '{1}', '{2}')".format(userphone, f_names, order))
        conn.commit()

    add_phone(phone, names, zakaz)
    c.execute('SELECT * FROM users')
    row = c.fetchone()
    while row is not None:
        print("id: " + str(row[0]) + " Phone: " + str(row[1]) + " Name: " + row[2] + " Call: " + row[3])
        row = c.fetchone()
    c.close()
    conn.close()
    ################## DATABASE #######################

    bot.register_next_step_handler(msg, site_back_7)

@bot.message_handler()
def sps8(message): #8
    """
    Процесс клика на кнопки "Прислать контакт"
    """
    #if message.text == pris_kont.text:
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('Сайт компании')
    keyboard.add('Подробнее')
    keyboard.add('/назад')
    msg = bot.send_message(message.chat.id,
                         'Спасибо, наши менеджеры свяжутся с Вами в ближайшее время!', reply_markup=keyboard)

    ################## DATABASE #######################
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    phone = message.contact.phone_number
    names = message.contact.first_name
    zakaz = 'Нужна консультация'
    try:
        c.execute(
            '''CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, phone VARCHAR, names VARCHAR, zakaz VARCHAR)''')
    except:
        print('--------------')

    def add_phone(userphone, f_names, order):
        c.execute(
            "INSERT INTO users(phone, names, zakaz)  VALUES ('{0}', '{1}', '{2}')".format(userphone, f_names, order))
        conn.commit()

    add_phone(phone, names, zakaz)
    c.execute('SELECT * FROM users')
    row = c.fetchone()
    while row is not None:
        print("id: " + str(row[0]) + " Phone: " + str(row[1]) + " Name: " + row[2] + " Call: " + row[3])
        row = c.fetchone()
    c.close()
    conn.close()
    ################## DATABASE #######################

    bot.register_next_step_handler(msg, site_back_8)

@bot.message_handler()
def end_click_1(message): #1
    """
    Процесс клика на кнопки "Заказать звонок, Подробнее, Назад"
    """
    if message.text == 'Заказать звонок':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        pris_kont = types.KeyboardButton(text="Прислать контакт", request_contact=True)
        keyboard.add(pris_kont)
        msg = bot.send_message(message.chat.id, 'Пожалуйста, укажите контактный телефон: как пример, 89********** или нажмите на кнопку «Прислать контакт».', reply_markup=keyboard)
        bot.register_next_step_handler(msg, sps)
    #if message.text == 'Назад':
        #msg = bot.send_message(message.chat.id, '/назад')
        #bot.register_next_step_handler(msg, menu)  # Два клика/исправить
    if message.text == "Подробнее":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru/services/auditorskie-uslugi/',reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)

@bot.message_handler()
def end_click_2(message): #2
    """
    Процесс клика на кнопки "Заказать звонок, Подробнее, Назад"
    """
    if message.text == 'Заказать звонок':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        pris_kont = types.KeyboardButton(text="Прислать контакт", request_contact=True)
        keyboard.add(pris_kont)
        msg = bot.send_message(message.chat.id, 'Пожалуйста, укажите контактный телефон: как пример, 89********** или нажмите на кнопку «Прислать контакт».', reply_markup=keyboard)
        bot.register_next_step_handler(msg, sps2)
    if message.text == 'Назад':
        msg = bot.send_message(message.chat.id, '/назад')
        bot.register_next_step_handler(msg, menu)  # Два клика/исправить
    if message.text == "Подробнее":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru/services/nalogovyy-i-bukhgalterskiy-konsalting/',reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)

@bot.message_handler()
def end_click_3(message): #3
    """
    Процесс клика на кнопки "Заказать звонок, Подробнее, Назад"
    """
    if message.text == 'Заказать звонок':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        pris_kont = types.KeyboardButton(text="Прислать контакт", request_contact=True)
        keyboard.add(pris_kont)
        msg = bot.send_message(message.chat.id, 'Пожалуйста, укажите контактный телефон: как пример, 89********** или нажмите на кнопку «Прислать контакт».', reply_markup=keyboard)
        bot.register_next_step_handler(msg, sps3)
    if message.text == 'Назад':
        msg = bot.send_message(message.chat.id, '/назад')
        bot.register_next_step_handler(msg, menu)  # Два клика/исправить
    if message.text == "Подробнее":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru/services/yuridicheskiy-konsalting/',reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)

@bot.message_handler()
def end_click_4(message): #4
    """
    Процесс клика на кнопки "Заказать звонок, Подробнее, Назад"
    """
    if message.text == 'Заказать звонок':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        pris_kont = types.KeyboardButton(text="Прислать контакт", request_contact=True)
        keyboard.add(pris_kont)
        msg = bot.send_message(message.chat.id, 'Пожалуйста, укажите контактный телефон: как пример, 89********** или нажмите на кнопку «Прислать контакт».', reply_markup=keyboard)
        bot.register_next_step_handler(msg, sps4)
    if message.text == 'Назад':
        msg = bot.send_message(message.chat.id, '/назад')
        bot.register_next_step_handler(msg, menu)  # Два клика/исправить
    if message.text == "Подробнее":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru/services/vedenie-bukhgalterskogo-ucheta/',reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)

@bot.message_handler()
def end_click_5(message): #5
    """
    Процесс клика на кнопки "Заказать звонок, Подробнее, Назад"
    """
    if message.text == 'Заказать звонок':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        pris_kont = types.KeyboardButton(text="Прислать контакт", request_contact=True)
        keyboard.add(pris_kont)
        msg = bot.send_message(message.chat.id, 'Пожалуйста, укажите контактный телефон: как пример, 89********** или нажмите на кнопку «Прислать контакт».', reply_markup=keyboard)
        bot.register_next_step_handler(msg, sps5)
    if message.text == 'Назад':
        msg = bot.send_message(message.chat.id, '/назад')
        bot.register_next_step_handler(msg, menu)  # Два клика/исправить
    if message.text == "Подробнее":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru/services/otsenka/',reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)

@bot.message_handler()
def end_click_6(message): #6
    """
    Процесс клика на кнопки "Заказать звонок, Подробнее, Назад"
    """
    if message.text == 'Заказать звонок':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        pris_kont = types.KeyboardButton(text="Прислать контакт", request_contact=True)
        keyboard.add(pris_kont)
        msg = bot.send_message(message.chat.id, 'Пожалуйста, укажите контактный телефон: как пример, 89********** или нажмите на кнопку «Прислать контакт».', reply_markup=keyboard)
        bot.register_next_step_handler(msg, sps6)
    if message.text == 'Назад':
        msg = bot.send_message(message.chat.id, '/назад')
        bot.register_next_step_handler(msg, menu)  # Два клика/исправить
    if message.text == "Подробнее":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru/services/obuchenie/',reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)

@bot.message_handler()
def end_click_7(message): #7
    """
    Процесс клика на кнопки "Заказать звонок, Подробнее, Назад"
    """
    if message.text == 'Заказать звонок':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        pris_kont = types.KeyboardButton(text="Прислать контакт", request_contact=True)
        keyboard.add(pris_kont)
        msg = bot.send_message(message.chat.id, 'Пожалуйста, укажите контактный телефон: как пример, 89********** или нажмите на кнопку «Прислать контакт».', reply_markup=keyboard)
        bot.register_next_step_handler(msg, sps7)
    if message.text == 'Назад':
        msg = bot.send_message(message.chat.id, '/назад')
        bot.register_next_step_handler(msg, menu)  # Два клика/исправить
    if message.text == "Подробнее":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru/services/it-konsalting/',reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)

@bot.message_handler()
def end_click_8(message): #8
    """
    Процесс клика на кнопки "Заказать звонок, Подробнее, Назад"
    """
    if message.text == 'Заказать звонок':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        pris_kont = types.KeyboardButton(text="Прислать контакт", request_contact=True)
        keyboard.add(pris_kont)
        msg = bot.send_message(message.chat.id, 'Пожалуйста, укажите контактный телефон: как пример, 89********** или нажмите на кнопку «Прислать контакт».', reply_markup=keyboard)
        bot.register_next_step_handler(msg, sps8)
    if message.text == 'Назад':
        msg = bot.send_message(message.chat.id, '/назад')
        bot.register_next_step_handler(msg, menu)  # Два клика/исправить
    if message.text == "Подробнее":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru/services/it-konsalting/',reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)

@bot.message_handler()
def buh_usl(message):#1
    """
    Бухгалтерские услуги
    """
    if message.text == 'Аутсорсинг бухгалтерии':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('Заказать звонок')
        keyboard.add('Подробнее')
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'Предлагаем полный комплекс услуг по ведению бухгалтерского и налогового учета индивидуальным предпринимателям, российским и иностранным предприятиям, зарегистрированным на территории РФ.',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, end_click_4)
    elif message.text == 'Бухгалтерские консультации':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('Заказать звонок')
        keyboard.add('Подробнее')
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id,
                               'Стоимость консультации: 3 000 руб./час',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, end_click_4)

@bot.message_handler()
def kontakt(message):
    """
    Контакты
    """
    if message.text == "Сайт компании":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'https://audex.ru/',reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu)
    if message.text == 'Назад':
        msg = bot.send_message(message.chat.id, 'Назад')
        bot.register_next_step_handler(msg, menu)  # Два клика/исправить

@bot.message_handler()
def sites(message):
    if message.text == 'Назад':
        msg = bot.send_message(message.chat.id, 'Назад')
        bot.register_next_step_handler(msg, menu)  # Два клика/исправить


@bot.message_handler()
def main_menu(message):
    """
    Процесс клика на кнопки "УСЛУГИ"
    """
    #1
    if message.text == 'Аудит':
        keyboard = types.ReplyKeyboardMarkup(selective=False)
        keyboard.add('Заказать звонок')
        keyboard.add('Подробнее')
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id, 'Компания «Аудэкс» - региональный лидер на аудиторском рынке. Компания входит  в ТОП-30 аудиторских компаний России и оказывает все виды аудита: \n\n_- обязательный и инициативный аудит\n- налоговый аудит\n- услуги по МСФО\n- услуги по МСФО\n- страховой аудит\n- аудит-контроллинг\n- инвестиционный аудит\n- комплаенс-аудит\n- форензик\n- due diligence и др._',
                               reply_markup=keyboard, parse_mode="Markdown")

        #msg_back = bot.send_message(message.chat.id, 'назад', reply_markup=keyboard)
        #bot.register_next_step_handler(msg_back, menu)

        bot.register_next_step_handler(msg, end_click_1)
    #2
    elif message.text == 'Налоговый консалтинг':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('Заказать звонок')
        keyboard.add('Подробнее')
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id,'Компания «Аудэкс» предлагает всестороннюю помощь в решении сложных бухгалтерских и налоговых вопросов. Консультанты предоставляют только аргументированные и безопасные рекомендации, что способствует защите ваших интересов и максимально исключает проблемы с налоговыми органами.\nУслуги:\n\n_- Налоговое сопровождение деятельности юридических лиц\n- Защита при возникновении налоговых споров\n- Защита налогоплательщика в налоговом арбитраже\n- Услуги по выявлению налоговых резервов и содействие возврату переплаты по налогам_',
                               reply_markup=keyboard, parse_mode="Markdown")
        bot.register_next_step_handler(msg, end_click_2)
    #3
    elif message.text == 'Юридические услуги':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('Заказать звонок')
        keyboard.add('Подробнее')
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id,'Команда разнопрофильных юристов компании «Аудэкс» решает вопросы в областях:\n\n_- корпоративного права\n- гражданско-правовых сделок\n- трудового права и кадрового учета\n- Представление интересов в Арбитражных судах\n- Консультации в области законодательства ПОД/ФТ_',
                               reply_markup=keyboard, parse_mode="Markdown")
        bot.register_next_step_handler(msg, end_click_3)
    #4
    elif message.text == 'Бухгалтерские услуги':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('Аутсорсинг бухгалтерии')
        keyboard.add('Бухгалтерские консультации')
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id,
                               '_- Аутсорсинг бухгалтерии и ведение бухгалтерского учета\n- Бухгалтерские консультации_',
                               reply_markup=keyboard,parse_mode="Markdown")
        bot.register_next_step_handler(msg, buh_usl)
    #5
    elif message.text == 'Оценка':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('Заказать звонок')
        keyboard.add('Подробнее')
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id,
                               '«Аудэкс» занимает ведущую позицию в сфере предоставления оценочных услуг. Департамент оценки «Аудэкс» специализируется на оказании широкого спектра услуг, связанных со стоимостной оценкой имущества и бизнеса.  Оценка проводится как в составе комплексных процедур (таких, например, как продажа предприятия, или приватизация), когда требуется оценка имущественного комплекса в целом, так и в виде оценки отдельных объектов недвижимости.\n*Оценка для физ.лиц:*\n\n_- Оценка квартир и домов\n- Оценка земельных участков\n- Оценка для Сбербанка\n- Оценка для ипотеки\n- Оценка для РОНО, нотариуса\n- Оценка мат.капитала и др._\n\n*Оценка для юр.лиц:*\n\n_- Оценка бизнеса\n- Оценка коммерческой недвижимости\n- Оценка машин и оборудования\n- Оценка права требования\n- Трансфертное ценообразование\n- Оценка интеллектуальной собственности_',
                               reply_markup=keyboard,  parse_mode="Markdown")
        bot.register_next_step_handler(msg, end_click_5)
    #6
    elif message.text == 'Обучение':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('Заказать звонок')
        keyboard.add('Подробнее')
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id,
                               'Фонд дополнительного профессионального образования "Аудэкс" - дочернее предприятие компании "Аудэкс" -предлагает программы по подготовке персонала финансовых, экономических, кадровых и юридических служб предприятия.\n\n_- Обучение бухгалтеров\n- Обучение аудиторов\n- Обучение адвокатов\n- Проведение Целевого инструктажа или повышение уровня знаний по ПОД/ФТ с выдачей Свидетельства\n- Тренинги_',
                               reply_markup=keyboard, parse_mode="Markdown")
        bot.register_next_step_handler(msg, end_click_6)
    #7
    elif message.text == 'Автоматизация бизнеса':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('Заказать звонок')
        keyboard.add('Подробнее')
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id,
                               'Услуги Департамента Автоматизации компании *«Аудэкс»*:\n\n_- Программное обеспечение 1С\n- Сопровождение и настройка 1С\n- 1С: ИТС\n- 1С в облаке\n- Деловое программное обеспечение\n- Обслуживание компьютерной сети_',
                               reply_markup=keyboard, parse_mode="Markdown")
        bot.register_next_step_handler(msg, end_click_7)
    #8
    elif message.text == 'Нужна консультация':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('Заказать звонок')
        keyboard.add('Подробнее')
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id,
                               'Стоимость консультации: 3 000 р/час',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, end_click_8)
    #9
    elif message.text == 'Контакты':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('Сайт компании')
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id,
                               'Аудиторско-консалтинговая компания *“Аудэкс”*\nТелефон: *+ 7 (843)20-20-760*\nE-mail: *info@audex.ru*\nАдрес: *г. Казань, ул. Подлужная, 60*\n_Дополнительный офис по оценке жилой недвижимости_\n*Ул. Гвардейская, 15, 7 этаж, оф.710*',
                               reply_markup=keyboard, parse_mode="Markdown")
        bot.register_next_step_handler(msg, kontakt)
    #10
    elif message.text == 'Сайт':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('/назад')
        msg = bot.send_message(message.chat.id,
                               'https://audex.ru',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, sites)

if __name__ == '__main__':
    bot.enable_save_next_step_handlers(delay=2)
    bot.load_next_step_handlers()
    bot.polling(none_stop=True)