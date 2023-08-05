import time
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import InputMediaPhoto
import gspread

bot = telebot.TeleBot('6461912908:AAHdvrRCa1gbrOHgAx7pyLNQjTTMsiSTEl8');

markupR = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("и тебе привет")
markupR.add(button1)

markupI = InlineKeyboardMarkup()
markupI.add(InlineKeyboardButton("text", callback_data="qwe"))



@bot.message_handler(commands='start')
def handle(message):
    firstnum = bot.send_message(message.chat.id, 'enter first number')
    bot.register_next_step_handler(firstnum, num1)

def num1(message):
    global number1;
    number1 = message.text
    secondnum = bot.send_message(message.chat.id, 'enter second number')
    bot.register_next_step_handler(secondnum, operator)

def operator(message):
    global number2;
    number2 = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itenbut1 = types.KeyboardButton('+')
    itenbut2 = types.KeyboardButton('-')
    itenbut3 = types.KeyboardButton('*')
    itenbut4 = types.KeyboardButton('/')
    markup.add(itenbut1, itenbut2, itenbut3, itenbut4)
    oper = bot.send_message(message.chat.id, 'enter operation', reply_markup=markup)
    bot.register_next_step_handler(oper, operat)

def operat(message):
    global op;
    op = message.text;
    markup = types.ReplyKeyboardRemove(selective=False)
    if op == '+':
        result = int(number1) + int(number2)
        bot.send_message(message.chat.id, result)
    elif op == '-':
        result = int(number1) - int(number2)
        bot.send_message(message.chat.id, result)
    elif op == '*':
        result = int(number1) * int(number2)
        bot.send_message(message.chat.id, result)
    elif op == '/':
        result = int(number1) / int(number2)
        bot.send_message(message.chat.id, result)
    else:
        bot.send_message(message.chat.id, 'error')
bot.polling(none_stop=True)

print("Ready")
bot.infinity_polling()
