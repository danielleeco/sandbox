import telebot
import logging

bot = telebot.TeleBot("1378818046:AAE2SaS-tPq0Z367dl6kgm3k8t0SOtnOSOE")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['id'])
def send_id(message):
	bot.reply_to(message, message.chat.id)
	

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	logging.error(message)
	bot.reply_to(message, message.text)


bot.polling()
