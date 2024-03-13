# import telebot 
# from telebot import types
# import random

# token = '6288304185:AAECbJLsy15HTbgJwNg_yWFOl0aaiY0BMTw'
# bot = telebot.TeleBot(token)
# keyboard = types.ReplyKeyboardMarkup()
# btn1 = types.KeyboardButton('Играть!')
# btn2 = types.KeyboardButton('Нет, я Пас!')
# keyboard.add(btn1, btn2 )

# @bot.message_handler(commands=['start', 'game'])
# def srart_message(message):
#     bot_message = bot.send_message(message.chat.id, 'Привет чемпион, начнем игру?', reply_markup=keyboard)
#     bot.register_next_step_handler(bot_message, check_answer)


# def check_answer(message):
#     if message.text == 'Играть!':
#         bot.send_message(message.chat.id, 'Ok, тогда лови правила игры:\nНужно угадать число, которое я загадаю в диапазоне от 1 до 10 вкючительно! У тебя будет 3 попытки! Если не угадаешь я тебя повешу! :)')
#         number = random.randint(1,10)
#         print(number)
#         game(message, 3, number)
#     elif message.text == 'Нет так нет, Пока!':
#         bot.send_message(message.chat.id, 'Нет так нет Пока!')
#     else:
#         bot_message = bot.send_message(message.chat.id, 'Вы ввели неправильный ответ!\nВведите снова: ', reply_markup = keyboard)
        
#         bot.register_next_step_handler(bot_message, check_answer)


# def game(message, attempts, number):
#     message_bot = bot.send_message(message.chat.id, 'Угадай число: ')
#     bot.register_next_step_handler(message_bot, check_answer, attempts-1, number)
    


# def check_number(message, attempts,number):
#     if message.text == str(number):
#         bot.send_message(message.chat.id, 'Вы победили!!')
#     elif attempts == 0:
#         bot.send_message(message.chat.id, 'You\'ve lost again and again!\n But you\'re still looking at your dream!\nIt\'s not over until you win!')
#     else:
#         bot.send_message(message.chat.id, f'Нет ты не угодал число, попробуй еще раз({attempts})!')
#         game(message, attempts, number)




# bot.polling()

import telebot
from telebot import types
import random

token = '6288304185:AAECbJLsy15HTbgJwNg_yWFOl0aaiY0BMTw'

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('Play')
btn2 = types.KeyboardButton('No Play')
keyboard.add(btn1, btn2)


@bot.message_handler(commands=['start', 'game'])
def start_message(message):
    bot_message = bot.send_message(message.chat.id, 'Hello, Champion! Wanna start a game?', reply_markup=keyboard)
    bot.register_next_step_handler(bot_message, check_answer)

def check_answer(message):
    if message.text == 'Play':
        bot.send_message(message.chat.id, 'Ok, тогда лови правила игры:\nНужно угадать число, которое я загадаю в диапазоне от 1 до 10 вкючительно! У тебя будет 3 попытки! Если не угадаешь я тебя повешу! :)')
        number = random.randint(1, 10)
        print(number)
        game(message, 3, number)
    elif message.text == 'No Play':
        bot.send_message(message.chat.id, 'No then no. Tschuess')
    else: 
        bot_message = bot.send_message(message.chat.id, 'Wrong number. Try again!.', reply_markup=keyboard)
        bot.register_next_step_handler(bot_message, check_answer)


def game(message, attempts, number):
    message_bot = bot.send_message(message.chat.id, 'Guess number: ')
    bot.register_next_step_handler(message_bot, ckeck_number, attempts-1, number) 

def ckeck_number(message, attempts, number):
    if message.text == str(number):
        bot.send_message(message.chat.id, 'You have a luck!')
    elif attempts == 0:
        bot.send_message(message.chat.id, 'You\'ve lost! Next time you shoot')
    else:
        bot.send_message(message.chat.id, f'Wrong answer. You have {attempts} yet')
        game(message,attempts, number)
bot.polling()
