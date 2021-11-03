import telebot;
from telebot import types;
import requests
import json
from random import randint
from telebot.types import InputMediaPhoto



bot = telebot.TeleBot('2024548148:AAE238nVxzWO6eva1N-dTBDZeKwnKnNawkk');
TELEGRAM_SUPPORT_CHAT_ID = -668427663

keyboard1 = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard1.row('Чат', 'Q&A', 'Тех. поддержка')



@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, '*Привет '+message.from_user.first_name + '!* Добро пожаловать в онлайн поддержку',  parse_mode= "Markdown", reply_markup=keyboard1)
    user_info = message.from_user.to_dict()

    bot.send_message(
        chat_id=TELEGRAM_SUPPORT_CHAT_ID,
        text=f"Присоеденился новый пользователь {message.from_user.first_name} {message.from_user.last_name}.",
    )
@bot.message_handler(content_types=['text'])
def get_text_message(message):
    global support
    if(message.chat.id == TELEGRAM_SUPPORT_CHAT_ID and message.reply_to_message != None):
        support = False
        user_id = message.reply_to_message.forward_from.id
        bot.send_message(
            chat_id=user_id,
            text=message.text
        )
    elif(message.text=='Чат'):
        support =False
        bot.send_message(message.chat.id, text='Наше дружное комьюнити!❤ \nhttps://t.me/joinchat/Fc7rOEQHceA0YjVi', reply_markup=keyboard1)
    elif (message.text=='Q&A'):
        support =False
        bot.send_message(message.chat.id, text='Вопрос1 - Ответ1 \nВопрос2 - Ответ2 \nВопрос3 - Ответ3 \nВопрос4 - Ответ4 \n', reply_markup=keyboard1)
    elif (message.text == 'Тех. поддержка'):
        support=True
        bot.send_message(message.chat.id, text='Если у вас имеются какие-либо вопросы - напишите ниже')
    else:
        if support == True:
            bot.forward_message(TELEGRAM_SUPPORT_CHAT_ID, message.chat.id, message.message_id)
            bot.send_message(message.chat.id, text='Спасибо за вопрос, ожидайте ответа оператора!')
            support =False
        else:
            bot.send_message(message.chat.id, text='Для навигации используйте меню!')




print("TgBot started")
bot.polling(none_stop=True, interval=1);
