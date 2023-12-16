import os
import maya
import telebot as tl

maya_obj = maya.Maya()
tg_bot = tl.TeleBot(os.getenv('BOT_TOKEN'))

@tg_bot.message_handler(commands=['start'])
def start(msg):
    tg_bot.send_message(msg.chat.id, "Привіт, мене звати Майя і я віртуальний статевий-терапевт. Ви можете задати будь-які питання, і я постараюся на них відповісти.")

@tg_bot.message_handler(commands=['help'])
def help(msg):
    tg_bot.send_message(msg.chat.id, "Ласкаво просимо до Майї, вашого віртуального статевого-терапевта. Ми тут, щоб надати безпечний та конфіденційний простір для ваших питань, пов'язаних із статевим здоров'ям та благополуччям.\n\nМайя призначена для надання інформації та підтримки без осуду. Не соромтеся вводити свої питання чи стурбованості у чат, і Майя зробить все можливе, щоб надати корисні та інформативні відповіді.\n\nЯкщо ваші проблеми тривають чи у вас є конкретне технічне запитання, будь ласка, зверніться до нашої служби технічної підтримки за електронною адресою marksadpepe@gmail.com.")

@tg_bot.message_handler(content_types='text')
def reply(msg):
    if msg.text[0] != '/':
        res = maya_obj.send_message_and_get_content(message=msg.text)
        tg_bot.send_message(msg.chat.id, res)

tg_bot.infinity_polling()