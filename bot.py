import os
import maya
import telebot as tl

maya_obj = maya.Maya()
tg_bot = tl.TeleBot(os.getenv('BOT_TOKEN'))

@tg_bot.message_handler(commands=['start'])
def start(msg):
    tg_bot.send_message(msg.chat.id, "Hi, my name is Maya and i'm  the virtual sex therapist. You can ask any questions and I will try to answer them")

@tg_bot.message_handler(commands=['help'])
def help(msg):
    tg_bot.send_message(msg.chat.id, "Welcome to Maya, your virtual sex therapist. We are here to provide a safe and confidential space for you to ask any questions related to your sexual health and well-being.\n\nMaya is designed to offer information and support in a non-judgmental manner. Feel free to type your questions or concerns in the chat, and Maya will do its best to provide helpful and informative responses.\n\nIf your issue persists or if you have a specific technical inquiry, please contact our technical support team via email at marksadpepe@gmail.com.")

@tg_bot.message_handler(content_types='text')
def reply(msg):
    if msg.text[0] != '/':
        res = maya_obj.send_message_and_get_content(message=msg.text)
        tg_bot.send_message(msg.chat.id, res)

tg_bot.infinity_polling()