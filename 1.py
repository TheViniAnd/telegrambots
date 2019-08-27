
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
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Старт", callback_data="test")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Здравствуйте! Здесь Вы можете записаться на консультацию или узнать подробнее об услугах компании. Нажмите Старт. ", reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        if call.message:
            if call.data == "test":
                keyboard = types.InlineKeyboardMarkup()
                np_button = types.InlineKeyboardButton(text="Нужна консультация", callback_data="np")
                keyboard.add(np_button)

                au_button = types.InlineKeyboardButton(text="Аудит", callback_data="au")
                keyboard.add(au_button)

                na_button = types.InlineKeyboardButton(text="Налоговый консалтинг", callback_data="na")
                keyboard.add(na_button)

                yr_button = types.InlineKeyboardButton(text="Юридические услуги", callback_data="yr")
                keyboard.add(yr_button)

                bu_button = types.InlineKeyboardButton(text="Бухгалтерские услуги", callback_data="bu")
                keyboard.add(bu_button)

                oc_button = types.InlineKeyboardButton(text="Оценка", callback_data="oc")
                keyboard.add(oc_button)

                obu_button = types.InlineKeyboardButton(text="Обучение", callback_data="obu")
                keyboard.add(obu_button)

                site_button = types.InlineKeyboardButton(text="Наш сайт", callback_data="site")
                keyboard.add(site_button)
                names = call.message.chat.first_name
                bot.send_message(call.message.chat.id,
                             names + ", здравствуйте!\n\nЯ онлайн-помощник компании «Аудэкс» - крупнейшей региональной аудиторско-консалтинговой компании России. Мы помогаем бизнесу принимать правильные решения уже 25 лет.\n\nКакая услуга Вас интересует? ",
                             reply_markup=keyboard)



            if call.message:
                if call.data == "np":
                    keyboard = types.InlineKeyboardMarkup()
                    date_button = types.InlineKeyboardButton(text="Выбрать дату", callback_data="date")
                    keyboard.add(date_button)
                    bot.send_message(call.message.chat.id,
                            "Консультация платная.\n\nСтоимость: 3 000 р. \n",
                            reply_markup=keyboard)

            if call.message:
                if call.data == "date":
                    bot.send_message(call.message.chat.id,
                                     "Пожалуйста, укажите контактный тел.")
                    @bot.message_handler(content_types=['text'])
                    def calendar_test(message):
                        inline_calendar.init(message.from_user.id,
                                             datetime.date.today(),
                                             datetime.date(year=2019, month=1, day=1),
                                             datetime.date(year=2020, month=12, day=31))


                        msg = bot.send_message(message.from_user.id, text='Пожалуйста, выберете дату.',
                                         reply_markup=inline_calendar.get_keyboard(message.from_user.id))

                    #bot.register_next_step_handler(msg, calendar_callback_handler)

                #@bot.callback_query_handler(func=lambda call: True) #func=inline_calendar.is_inline_calendar_callbackquery)
                #def calendar_callback_handler(calls):
                #    bot.answer_callback_query(calls.id)
                #    print(calls)
#
#                    try:
#                        return_data = inline_calendar.handler_callback(calls.from_user.id, calls.data)
#                        print('es')
#                        if return_data is None:
#                            print('es')
#                        else:
#                            print(return_data)
#                    except:
#                        print('except')
                        #bot.edit_message_text(text='Ошибка', chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=inline_calendar.get_keyboard(call.from_user.id))


                    @bot.callback_query_handler(func=lambda call: True)  # func=inline_calendar.is_inline_calendar_callbackquery)
                    def calendar_callback_handler(call):
                        bot.answer_callback_query(call.id)
                        try:
                            print('try')
                            return_data = inline_calendar.handler_callback(call.from_user.id, call.data)
                            if return_data is None:
                                bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                                              message_id=call.message.message_id,
                                                              reply_markup=inline_calendar.get_keyboard(
                                                                  call.from_user.id))
                            else:
                                picked_data = return_data
                                bot.send_message(text=picked_data, chat_id=call.from_user.id)

                        except inline_calendar.WrongChoiceCallbackException:
                            bot.edit_message_text(text='Ошибка', chat_id=call.from_user.id,
                                                  message_id=call.message.message_id,
                                                  reply_markup=inline_calendar.get_keyboard(call.from_user.id))

                if call.data == "au":
                    keyboard = types.InlineKeyboardMarkup()
                    vopros_button = types.InlineKeyboardButton(text="Есть вопросы по услуге?", callback_data="vopros")
                    keyboard.add(vopros_button)
                    bot.send_message(call.message.chat.id,
                            "Компания «Аудэкс» - региональный лидер на аудиторском рынке.\nКомпания входит в  оказывает все виды аудита:\n"
                            "\n- Обязательный и инициативный аудит\n- Налоговый аудит\n- Аудит-контроллинг\n- инвестиционный аудит\n- комплаенс-аудит\n- форензик \n- due diligence",
                            reply_markup=keyboard)

                if call.data == "na":
                    keyboard = types.InlineKeyboardMarkup()
                    vopros_button = types.InlineKeyboardButton(text="Есть вопросы по услуге?", callback_data="vopros")
                    keyboard.add(vopros_button)
                    bot.send_message(call.message.chat.id,
                                 "Компания «Аудэкс» предлагает всестороннюю помощь в решении сложных бухгалтерских и налоговых вопросов.\n\n"
                                 "Наши консультанты предоставляют только аргументированные и безопасные рекомендации, что способствует защите ваших интересов и максимально исключает проблемы с налоговыми органами.\n\nНаши услуги:\n\n- Налоговое сопровождение деятельности юридических лиц\n- Защита при возникновении налоговых споров\n- Защита налогоплательщика в налоговом арбитраже\n- Услуги по выявлению налоговых резервов и содействие возврату переплаты по налогам",
                                 reply_markup=keyboard)

                if call.data == "yr":
                    keyboard = types.InlineKeyboardMarkup()
                    vopros_button = types.InlineKeyboardButton(text="Есть вопросы по услуге?", callback_data="vopros")
                    keyboard.add(vopros_button)
                    bot.send_message(call.message.chat.id,
                                 "Команда юристов компании «Аудэкс» поможет решить вопросы в областях:\n\n"
                                 "Юридические услуги\n\n- Корпоративного права\n- Трудового права и кадрового учета\n- Трансфертного ценообразования\n- Представление интересов в Арбитражных судах\n- Консультации в области законодательства ПОД/ФТ\n",
                                 reply_markup=keyboard)
            #Бухгалтерские услуги
                if call.data == "bu":
                    keyboard = types.InlineKeyboardMarkup()
                    vopros_button = types.InlineKeyboardButton(text="Есть вопросы по услуге?", callback_data="vopros")
                    keyboard.add(vopros_button)
                    bot.send_message(call.message.chat.id,
                                 "Бухгалтерские услуги\n\n- Аутсорсинг бухгалтерии \n- Ведение бухгалтерского учета\n- Бухгалтерские консультации",
                                 reply_markup=keyboard)

            #Оценка
                if call.data == "oc":
                    keyboard = types.InlineKeyboardMarkup()
                    vopros_button = types.InlineKeyboardButton(text="Есть вопросы по услуге?", callback_data="vopros")
                    keyboard.add(vopros_button)
                    bot.send_message(call.message.chat.id,
                                 "Оценка\n\n- Оценка бизнеса\n- Оценка машин и оборудования\n- Оценка для ипотеки \n- Оценка для РОНО, нотариуса\n- Оценка для мат.капитала",
                                 reply_markup=keyboard)

                if call.data == "obu":
                    keyboard = types.InlineKeyboardMarkup()
                    vopros_button = types.InlineKeyboardButton(text="Есть вопросы по услуге?", callback_data="vopros")
                    keyboard.add(vopros_button)
                    bot.send_message(call.message.chat.id,
                                 "Обучение\n\n- Обучение бухгалтеров \n- Обучение аудиторов\n- Обучение адвокатов\n- ПОДФТ\n- ВЭД",
                                 reply_markup=keyboard)

            #Открыть сайт
                if call.data == "site":
                    keyboard = types.InlineKeyboardMarkup()
                    site_button_two = types.InlineKeyboardButton(text="Наш сайт", url="https://audex.ru")
                    keyboard.add(site_button_two)
                    bot.send_message(call.message.chat.id,
                                 "Перейти на сайт ",
                                 reply_markup=keyboard)

                if call.message:
                    if call.data == "vopros":
                        bot.send_message(call.message.chat.id,
                                     "Пожалуйста, укажите контактный тел.")
                        @bot.message_handler(content_types=["text"])
                        def any_msg(message):

                            texts = str(message.text)
                            print(texts)
                            print(len(texts))
                            if len(texts) >= 11 and len(texts)<=12:
                                if texts[0] == '+':
                                    texts = texts[1:]
                                    if texts.isdigit():
                                        if len(texts) > 1 and len(texts) <= 11:
                                            print(
                                                'Имя:' + message.chat.first_name +
                                                ' Фамилия:' + message.chat.last_name +
                                                ' \nusername: ' + message.chat.username
                                            )
                                            conn = sqlite3.connect('phone.db')
                                            c = conn.cursor()
                                            phone = message.text
                                            first_name = message.chat.first_name
                                            last_name = message.chat.last_name
                                            username = message.chat.username
                                            try:
                                                c.execute('''CREATE TABLE users (id integer primary key AUTOINCREMENT, phone varchar)''')
                                            except:
                                                print('--------------')
                                            def add_phone(userphone):
                                                c.execute(
                                                    "INSERT INTO users(phone)  VALUES ('{0}')".format(userphone))
                                                conn.commit()


                                            add_phone(phone)
                                            c.execute('SELECT * FROM users')
                                            row = c.fetchone()
                                            while row is not None:
                                                print("id: " + str(row[0]) + " Телефон: " + row[1])
                                                row = c.fetchone()
                                            c.close()
                                            conn.close()
                                            keyboard = types.InlineKeyboardMarkup()
                                            bot.send_message(message.chat.id,
                                                     "Спасибо, Вы записаны. Наши менеджеры свяжутся с Вами. ")
                                            nsite_button = types.InlineKeyboardButton(text="Наш сайт", url="https://audex.ru")
                                            keyboard.add(nsite_button)
                                            bot.send_message(call.message.chat.id,
                                                         "Перейти на сайт ",
                                                         reply_markup=keyboard)
                                    else:
                                        bot.send_message(message.chat.id,'Некорректный номер')
                                else:
                                    if texts.isdigit():
                                        if len(texts) > 1 and len(texts) <= 11:
                                            print(
                                                'Имя:' + message.chat.first_name +
                                                ' Фамилия:' + message.chat.last_name +
                                                ' \nusername: ' + message.chat.username
                                            )
                                            conn = sqlite3.connect('phone.db')
                                            c = conn.cursor()
                                            phone = message.text
                                            first_name = message.chat.first_name
                                            last_name = message.chat.last_name
                                            username = message.chat.username
                                            try:
                                                c.execute('''CREATE TABLE users (id integer primary key AUTOINCREMENT, phone varchar)''')
                                            except:
                                                print('--------------')
                                            def add_phone(userphone):
                                                c.execute("INSERT INTO users(phone)  VALUES ('{0}')".format(userphone))
                                                conn.commit()

                                            add_phone(phone)
                                            c.execute('SELECT * FROM users')
                                            row = c.fetchone()
                                            while row is not None:
                                                print("id: " + str(row[0]) + " Телефон: " + row[1])  # + " Имя: " + row[2] + " Фамилия: " + row[3] + " Логин: " + row[4])
                                                row = c.fetchone()
                                            c.close()
                                            conn.close()

                                            keyboard = types.InlineKeyboardMarkup()
                                            bot.send_message(message.chat.id,
                                                     "Спасибо, Вы записаны. Наши менеджеры свяжутся с Вами. ")
                                            nsite_button = types.InlineKeyboardButton(text="Наш сайт", url="https://audex.ru")
                                            keyboard.add(nsite_button)
                                            bot.send_message(call.message.chat.id,
                                                     "Перейти на сайт ",
                                                     reply_markup=keyboard)
                                    else:
                                        bot.send_message(message.chat.id, 'Некорректный номер')
                            else:
                                bot.send_message(message.chat.id, "Некорректный номер")



if __name__ == '__main__':
    bot.infinity_polling(True)