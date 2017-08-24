import telebot, constants
import re
bot = telebot.TeleBot(constants.token)
# bot.send_message(1477790,"test")
# upd=bot.get_updates()
# print(upd)
# last_upd = upd[-1]
# message_from_user = last_upd.message
# print(message_from_user)



user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None









print(bot.get_me())
def log(message, answer):
    print("\n -----")
    from datetime import  datetime
    print(datetime.now())
    print("Message from {0} {1}. (id={2}) \n Text - {3}".format(message.from_user.first_name,
                                                                 message.from_user.last_name,
                                                                 str(message.from_user.id),
                                                                 message.text))
    print(answer)
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop', '/search')
    user_markup.row('photo', 'audio', 'documents')
    user_markup.row('sticker', 'video', 'location')
    bot.send_message(message.from_user.id, 'Welcome..', reply_markup=user_markup)
@bot.message_handler(content_types=["commands"])

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, '..', reply_markup=hide_markup)

def handle_command(message):
    print("Принята команда")

@bot.message_handler(commands=["help"])
def handle_text(message):
    print("Принята команда help")

@bot.message_handler(commands=["search"])
def handle_text(message):
    print("Принята команда search")
    msg = bot.reply_to(message, """\
    Hi there, I am Example bot.
    What's your name?
    """)
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, 'How old are you?')
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_age_step(message):
    try:
        chat_id = message.chat.id
        age = message.text
        if not age.isdigit():
            msg = bot.reply_to(message, 'Age should be a number. How old are you?')
            bot.register_next_step_handler(msg, process_age_step)
            return
        user = user_dict[chat_id]
        user.age = age
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Male', 'Female')
        msg = bot.reply_to(message, 'What is your gender', reply_markup=markup)
        bot.register_next_step_handler(msg, process_sex_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_sex_step(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        user = user_dict[chat_id]
        if (sex == u'Male') or (sex == u'Female'):
            user.sex = sex
        else:
            raise Exception()
        bot.send_message(chat_id, 'Nice to meet you ' + user.name + '\n Age:' + str(user.age) + '\n Sex:' + user.sex)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(content_types=["document"])
def handle_document(message):
    print("document in message")

@bot.message_handler(content_types=["audio"])
def handle_audio(message):
    print("auido in message")

@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    print("photo in message")

@bot.message_handler(content_types=["sticker"])
def handle_sticker(message):
    print("sticker in message")

# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     answer = "Abby"
#     if message.text == 'a':
#         answer="AB"
#         bot.send_message(message.chat.id, answer)
#         log(message,answer)
#     elif message.text == 'b':
#         answer="BABB"
#         bot.send_message(message.chat.id, answer)
#         log(message,answer)
#     elif message.text == "?" and str(message.from_user.id)=="1477790":
#         answer = "Мои поздравления {0} !".format(message.from_user.first_name)
#         bot.send_message(message.chat.id,answer)
#     else:
#         bot.send_message(message.chat.id, message.text+answer+"!!!")







    print("text message")
bot.polling(none_stop=True, interval=0)