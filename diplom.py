# -*- coding: utf-8 -*-
import config
import datetime
import telebot

from telebot import apihelper, types
import sqlite3
import inline_calendar

apihelper.proxy = {'http':'http://10.10.1.10:3128'}

token = '******'
bot = telebot.TeleBot(token, threaded=False)





@bot.message_handler(commands=["start"])
def default_test(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('Старт')
    msg = bot.send_message(message.chat.id,text='Аптека Будущего Pharmaсy Concept Store - это уникальная сервисная европейская аптека где наши посетители могут получить профессиональные советы и консультации, приобрести нужные лекарства, а также профессиональную и лечебную косметику. Приятным дополнением к аптечному залу является Центр Красоты Beauty Care Centre, созданный с целью предоставления современных косметологических процедур и рекомендаций.',reply_markup=keyboard)
    bot.register_next_step_handler(msg, menu)

@bot.message_handler(func=lambda message: message.text == "Старт")
def menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('💡 Акции')
    keyboard.add('🔍 Заказать лекарство','💰 Получить скидку')
    keyboard.add('📖 Нужна консультация', '📞 Контакты')
    keyboard.add('Товары')
    msg = bot.send_message(message.chat.id, 'Какая услуга Вас интересует?', reply_markup=keyboard)
    bot.register_next_step_handler(msg, main_menu)


@bot.message_handler()
def site_back_1(message): #1
    if message.text == 'Назад':
        msg = bot.send_message(message.chat.id,'Вернуться назад?')
        bot.register_next_step_handler(msg, menu)#Два клика/исправить

@bot.message_handler()
def sps(message): #1
    """
    Процесс клика на кнопки "Прислать контакт"
    """
    if message.text == 'Назад':
        msg = bot.send_message(message.chat.id, 'Вернуться назад?')
        bot.register_next_step_handler(msg, menu)  # Два клика/исправить
    else:
        import random
        random_code =random.randint(1000, 3000)
        sale = random.randint(1, 30)
        skidka = 'Спасибо, ваш код активации: '+ str(random_code) + '. Скидка ' +str(sale) + '%'
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('Назад')
        msg = bot.send_message(message.chat.id, skidka, reply_markup=keyboard)

        ################## DATABASE #######################
        conn = sqlite3.connect('diplom.db')
        c = conn.cursor()
        try:
            phone = message.contact.phone_number
            names = message.contact.first_name
        except:
            phone = '0000000000'
            names = 'none'

        try:
            c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, phone VARCHAR, names VARCHAR)''')
        except:
            print('--------------')

        def add_phone(userphone, f_names):
            c.execute(
                "INSERT INTO users(phone, names)  VALUES ('{0}', '{1}')".format(userphone, f_names))
            conn.commit()

        add_phone(phone, names)
        c.execute('SELECT * FROM users')
        row = c.fetchone()
        while row is not None:
            print("id: " + str(row[0]) + " Phone: " + str(row[1]) + " Name: " + row[2])
            row = c.fetchone()
        c.close()
        conn.close()
        ################## DATABASE #######################

        bot.register_next_step_handler(msg, site_back_1)



@bot.message_handler()
def end_click_1(message): #1
    """
    Процесс клика на кнопки "Заказать звонок, Подробнее, Назад"
    """
    if message.text == 'Назад':
        msg = bot.send_message(message.chat.id, 'Вернуться назад?')
        bot.register_next_step_handler(msg, menu)  # Два клика/исправить


@bot.message_handler()
def end_click_2(message): #2
    """
    Процесс клика на кнопки "Заказать звонок, Подробнее, Назад"
    """
    if message.text == 'Назад':
        msg = bot.send_message(message.chat.id, 'Вернуться назад?')
        bot.register_next_step_handler(msg, menu)  # Два клика/исправить
    else:
        mes = message.text
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('Назад')

        msg = bot.send_message(message.chat.id, 'Ваш заказ принят, вам перезвонят. \n\n'+mes,
                               reply_markup=keyboard, parse_mode="Markdown")
        bot.register_next_step_handler(msg, end_click_2)



@bot.message_handler()
def buh_usl(message):
    """
    Бухгалтерские услуги
    """
    if message.text == 'Назад':
        msg = bot.send_message(message.chat.id, 'Вернуться назад?')
        bot.register_next_step_handler(msg, menu)
    else:
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('Назад')
        msg = bot.send_message(message.chat.id, 'Спасибо, с вами свяжуться.', reply_markup=keyboard)
        bot.register_next_step_handler(msg, site_back_1)


@bot.message_handler()
def kontakt(message):
    """
    Контакты
    """
    if message.text == 'Назад':
        msg = bot.send_message(message.chat.id, 'Вернуться назад?')
        bot.register_next_step_handler(msg, menu)  # Два клика/исправить

def next_one(message):
    if message.text == 'Далее':
        keyboard = types.ReplyKeyboardMarkup(selective=False)
        keyboard.add('Назад')
        msg = bot.send_message(message.chat.id, '*Азопт*\n_Капли, 5 мл, 1 %_\n*Цена от от 350 ₽*\n\n'
                                                '*Аква-риносоль*\n_Спрей, 20 мл, 0,9 %_\n*Цена от 43,09 ₽*\n\n'
                                                '*Аквамастер*\n_50 мл, 0,65 %_\n*Цена 138 ₽*\n\n'
                                                '*Акинетон*\n_Таблетки, 100 шт, 2 мг_\n*Цена от 289 ₽*\n\n'
                                                '*Бидоп*\n_Таблетки, 28 шт, 5 мг_\n*Цена 86,85 ₽*\n\n'
                                                '*Бинафин*\n_Крем, 10 г, 1 %_\n*Цена от 151 ₽*\n\n'
                                                '*Блоктран*\n_Таблетки, 60 шт, 50 мг_\n*Цена от 324 ₽*\n\n'
                                                '*Валокордин*\n_Капли, 20 мл_\n*Цена от 67 ₽*\n\n'
                                                '*Валосердин*\n_Капли, 50 мл_\n*Цена от 118 ₽*\n\n',
                               reply_markup=keyboard, parse_mode="Markdown")
        bot.register_next_step_handler(msg, menu)

def tovar(message):
    if message.text == 'Лекарства и БАД':
        keyboard = types.ReplyKeyboardMarkup(selective=False)
        keyboard.add('Далее')
        keyboard.add('Назад')
        msg = bot.send_message(message.chat.id, '*Абактал*\n_Таблетки, 10 шт, 400 мг_\n*Цена от 245,50 ₽*\n\n'
                                                '*Авамис*\n_Спрей, 120 д, 27,5 мкг/доза, назальный_\n*Цена от 646 ₽*\n\n'
                                                '*Абакавир Канон*\n_Таблетки, 30 шт, 600 мг, в пленочной оболочке_\n*Цена 2130,90 ₽*\n\n'
                                                '*Авиамарин*\n_Таблетки, 10 шт, 50 мг_\n*Цена от 132 ₽*\n\n'
                                                '*Авекорт*\n_Мазь, туба, 15 г, 0,1 %, для наружного применения_\n*Цена 197,50 ₽*\n\n'
                                                '*Адвантан*\n_Крем, 15 г, 0,1 %_\n*Цена от 506 ₽*\n\n'
                                                '*Адаптол*\n_Таблетки, 20 шт, 500 мг_\n*Цена от 633,94 ₽*\n\n'
                                                '*Адепресс*\n_Таблетки, 30 шт, 20 мг_\n*Цена от 348 ₽*\n\n'
                                                '*Адисорд*\n_Капсулы, 20 шт, 200 мг_\n*Цена от 245 ₽*\n\n',
                               reply_markup = keyboard, parse_mode = "Markdown")
        bot.register_next_step_handler(msg, next_one)
    if message.text == 'Средства гигиены':
        keyboard = types.ReplyKeyboardMarkup(selective=False)
        keyboard.add('Назад')
        msg = bot.send_message(message.chat.id, '*Twin lotus мыло с алоэ вера и маслом авокадо*\n_Мыло, 80 г_\n*Цена от 80 ₽*\n\n'
                                                '*Twin lotus паста зубн. оригинальная с травами*\n_Зубная паста, 100 г_\n*Цена от 181 ₽*\n\n'
                                                '*Ангиосепт раствор для полости рта*\n_Раствор, флакон, 200 мл, для полости рта, календула_\n*Цена 199 ₽*\n\n'
                                                '*БиСи Салфетки влажные антибактериальные*\n_Салфетки, 20 шт_\n*Цена от 24 ₽*\n\n'
                                                '*Диадент ополаскиватель актив для полости рта*\n_Ополаскиватель, 250 мл_\n*Цена 85 ₽*\n\n'
                                                '*Гардекс Экстрим от клещей*\n_Спрей, флакон, 250 мл_\n*Цена от 359 ₽*\n\n',
                               reply_markup = keyboard, parse_mode = "Markdown")
        bot.register_next_step_handler(msg, menu)
    if message.text == 'Медицинские приборы':
        keyboard = types.ReplyKeyboardMarkup(selective=False)
        keyboard.add('Назад')
        msg = bot.send_message(message.chat.id, '*AND CN-233 ингалятор компрессорный*\n_Ингалятор, 1 шт_\n*Цена от 2116 ₽*\n\n'
                                                '*AND UA-100 тонометр механический*\n_Тонометр, 1 шт_\n*Цена от 772 ₽*\n\n'
                                                '*AND UA-1100 тонометр автоматический*\n_Тонометр, 1 шт, с гипоаллергенной манжетой_\n*Цена 3248 ₽*\n\n'
                                                '*PL бинт марлевый стерильный 5м х 10см*\n_Бинт, 1 шт, мед_\n*Цена 30 ₽*\n\n'
                                                '*PL медицинская маска*\n_Маска, 3 шт_\n*Цена 45 ₽*\n\n'
                                                '*PL Перчатки латексные нестерильные неопудренные*\n_Перчатки, 100 шт_\n*Цена от 272 ₽*\n\n'
                                                '*PL пластырь бактерицидный*\n_Пластырь, 1 шт_\n*Цена от 5 ₽*\n\n'
                                                '*Альпина спринцовка пвх с твердым наконечником N9*\n_Спринцовка, 230 мл_\n*Цена от 97 ₽*\n\n',
                               reply_markup = keyboard, parse_mode = "Markdown")
        bot.register_next_step_handler(msg, menu)
    if message.text == 'Питание и спорт':
        keyboard = types.ReplyKeyboardMarkup(selective=False)
        keyboard.add('Назад')
        msg = bot.send_message(message.chat.id, '*NFO Норвегиан фиш Омега-3 масло криля*\n_Капсулы, 60 шт, 1450 мг_\n*Цена от 1093 ₽*\n\n'
                                                '*PL Гематоген витаминизированный*\n_Гематоген, 40 г_\n*Цена 19 ₽*\n\n'
                                                '*PL Гематоген детский с курагой*\n_Гематоген, 40 г_\n*Цена 24 ₽*\n\n'
                                                '*PL Пустырник Премиум*\n_Пастилки, 25 г_\n*Цена 37 ₽*\n\n'
                                                '*PL Рыбий жир Микс вкусов*\n_Капсулы, 120 шт, для детей_\n*Цена 295 ₽*\n\n'
                                                '*Агуша Вода*\n_Вода, 330 мл_\n*Цена 39 ₽*\n\n'
                                                '*Биафишенол рыбий жир*\n_Капсулы, 100 шт, с облепиховым маслом и витамином е_\n*Цена от 66 ₽*\n\n'
                                                '*Тмин плоды*\n_Плоды, 50 г_\n*Цена от 20,50 ₽*\n\n',
                               reply_markup = keyboard, parse_mode = "Markdown")
        bot.register_next_step_handler(msg, menu)
    if message.text == 'Косметика':
        keyboard = types.ReplyKeyboardMarkup(selective=False)
        keyboard.add('Назад')
        msg = bot.send_message(message.chat.id, '*911 витаминный*\n_Шампунь, 150 мл, для восстановления волос_\n*Цена от 110 ₽*\n\n'
                                                '*Weleda масло березовое*\n_Масло, флакон, 100 мл_\n*Цена от 1204,27 ₽*\n\n'
                                                '*Weleda масло дикой розы*\n_Масло, 100 мл, для лица, интенсивное_\n*Цена 1477 ₽*\n\n'
                                                '*Weleda молочко для тела облепиховое питающее*\n_Молочко, флакон, 200 мл, для тела, облепиха_\n*Цена от 930 ₽*\n\n'
                                                '*Woshi-woshi диски ватные*\n_Ватные диски, 80 шт_\n*Цена 83 ₽*\n\n'
                                                '*Weleda Эверон бальзам для губ*\n_Бальзам, 4,8 г, для губ_\n*Цена от 299,48 ₽*\n\n'
                                                '*Авен клинанс вода очищающая*\n_Вода, 400 мл_\n*Цена от 1013 ₽*\n\n'
                                                '*Аванта помада гигиеническая облепиховая в футляре*\n_Помада, 2 г_\n*Цена от 17 ₽*\n\n',
                               reply_markup = keyboard, parse_mode = "Markdown")
        bot.register_next_step_handler(msg, menu)
    if message.text == 'Назад':
        msg = bot.send_message(message.chat.id, 'Вернуться назад?')
        bot.register_next_step_handler(msg, menu)

@bot.message_handler()
def main_menu(message):
    """
    Процесс клика на меню
    """
    #1
    if message.text == '💡 Акции':
        keyboard = types.ReplyKeyboardMarkup(selective=False)
        keyboard.add('Назад')
        msg = bot.send_message(message.chat.id, '*Акции этого месяца*\n\n_-Специальные цены на серию для волос_ *Dr. Sante «Жидкий шелк»*\n'
                                                '-_Специальная цена на_ *Lactoflorene® Холестерол*\n'
                                                '-_Специальные цены на косметику_ *Yoghurt of bulgaria*\n'
                                                '_-Специальные цены на_ *обезболивающее Сафистон®*\n'
                                                '_-Специальные цены на средства по уходу за кожей_ *TENA*'
                                                '\n\nКаждый месяц Акции будут обновляться.', reply_markup=keyboard, parse_mode="Markdown")
        bot.register_next_step_handler(msg, end_click_1)
    #2
    elif message.text == '🔍 Заказать лекарство':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('Назад')
        msg = bot.send_message(message.chat.id, 'Напишите названия лекарства, количество и номер телефона.\n\n*Например*\n\n_Глицин, 1 упаковка. +79192212121_',
                               reply_markup=keyboard, parse_mode="Markdown")
        bot.register_next_step_handler(msg, end_click_2)
    #3
    elif message.text == '💰 Получить скидку':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

        names = message.chat.first_name
        #####database######
        conn = sqlite3.connect('diplom.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users')
        row = c.fetchone()
        a = False
        while row is not None:
            if names == row[2]:
                a = True
            row = c.fetchone()
        c.close()
        conn.close()
        ##################
        if a == False:
            pris_kont = types.KeyboardButton(text="Получить скидку", request_contact=True)

            keyboard.add(pris_kont)
        else:
            print('')

        keyboard.add('Назад')
        msg = bot.send_message(message.chat.id,'Получить скидку можно после подписки на уведомления. \n\n\n\n _Активировать скидку можно только один раз._',
                               reply_markup=keyboard, parse_mode="Markdown")
        bot.register_next_step_handler(msg, sps)
    #4
    elif message.text == '📖 Нужна консультация':
        keyboard = types.ReplyKeyboardMarkup()
        pris_kont = types.KeyboardButton(text="Прислать номер", request_contact=True)
        keyboard.add(pris_kont)
        keyboard.add('Назад')
        msg = bot.send_message(message.chat.id,
                               'Записаться на консультацию. \n\n _Вам перезвонт в ближайшее время_',
                               reply_markup=keyboard,parse_mode="Markdown")
        bot.register_next_step_handler(msg, buh_usl)

    #5
    elif message.text == '📞 Контакты':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('Назад')
        msg = bot.send_message(message.chat.id,
                               '*Наши контакты:*\n\nТелефон: *+ 7 (999)00-00-000*\n\nE-mail: *info@audex.ru*\n\nАдрес: *г. Казань, ул. Подлужная, 60*',
                               reply_markup=keyboard, parse_mode="Markdown")
        bot.register_next_step_handler(msg, kontakt)

    elif message.text == 'Товары':
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add('Лекарства и БАД')
        keyboard.add('Средства гигиены')
        keyboard.add('Косметика')
        keyboard.add('Медицинские приборы')
        keyboard.add('Питание и спорт')
        keyboard.add('Назад')
        msg = bot.send_message(message.chat.id,
                               'Товары распределенны по категориям:',
                               reply_markup=keyboard, parse_mode="Markdown")
        bot.register_next_step_handler(msg, tovar)

if __name__ == '__main__':
    bot.enable_save_next_step_handlers(delay=2)
    bot.load_next_step_handlers()
    bot.polling(none_stop=True)
