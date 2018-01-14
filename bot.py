import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging
import time
from telegram import InlineQueryResultArticle, ChatAction, InputTextMessageContent
import calendar
from datetime import date

import requests
from bs4 import BeautifulSoup
import random
import datetime
import emoji
import urllib.request
import json

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import time





bot = telegram.Bot(token='536898310:AAHmGVSAniSKvzouu8-TVrTx2qqiGzaX7qE')
updater = Updater(token='536898310:AAHmGVSAniSKvzouu8-TVrTx2qqiGzaX7qE')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater.start_polling()

def start(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text= "Welcome to Fiverbot! \nType /founder to find out who the founders of fiverr are \nType /history to get which year fiverr was founded \nType /noofusers to find out how many users currently use Fiverr \nType /location to find out the location of headquarters of Fiverr \nType /number to get Fiverr's corporate phone number\nType /email to get Fiverr's email")
                       
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def founder(bot, update):
    
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id,text="Shai Wininger and Micha Kaufman")
    bot.sendMessage(chat_id=update.message.chat_id, text= "Type /founder to find out who the founders of fiverr are \nType /history to get which year fiverr was founded \nType /noofusers to find out how many users currently use Fiverr \nType /location to find out the location of headquarters of Fiverr \nType /number to get Fiverr's corporate phone number\nType /email to get Fiverr's email")
        
founder_handler = CommandHandler('founder', founder)
dispatcher.add_handler(founder_handler)

def history(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    
    bot.sendMessage(chat_id=update.message.chat_id,text="February 1, 2010")
    bot.sendMessage(chat_id=update.message.chat_id, text= "Type /founder to find out who the founders of fiverr are \nType /history to get which year fiverr was founded \nType /noofusers to find out how many users currently use Fiverr \nType /location to find out the location of headquarters of Fiverr \nType /number to get Fiverr's corporate phone number\nType /email to get Fiverr's email")
      
history_handler = CommandHandler('history', history)
dispatcher.add_handler(history_handler)

def noofusers(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    
    bot.sendMessage(chat_id=update.message.chat_id,text="14 million users")
    bot.sendMessage(chat_id=update.message.chat_id, text= "Type /founder to find out who the founders of fiverr are \nType /history to get which year fiverr was founded \nType /noofusers to find out how many users currently use Fiverr \nType /location to find out the location of headquarters of Fiverr \nType /number to get Fiverr's corporate phone number\nType /email to get Fiverr's email")
      
noofusers_handler = CommandHandler('noofusers', noofusers)
dispatcher.add_handler(noofusers_handler)

def location(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    
    bot.sendMessage(chat_id=update.message.chat_id,text="3514 International Drive Northwest Washington, DC 20008 USA")
    bot.sendMessage(chat_id=update.message.chat_id, text= "Type /founder to find out who the founders of fiverr are \nType /history to get which year fiverr was founded \nType /noofusers to find out how many users currently use Fiverr \nType /location to find out the location of headquarters of Fiverr \nType /number to get Fiverr's corporate phone number\nType /email to get Fiverr's email")
      
location_handler = CommandHandler('location', location)
dispatcher.add_handler(location_handler)

def number(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    
    bot.sendMessage(chat_id=update.message.chat_id,text="72-54-484-3988")
    bot.sendMessage(chat_id=update.message.chat_id, text= "Type /founder to find out who the founders of fiverr are \nType /history to get which year fiverr was founded \nType /noofusers to find out how many users currently use Fiverr \nType /location to find out the location of headquarters of Fiverr \nType /number to get Fiverr's corporate phone number\nType /email to get Fiverr's email")
      
number_handler = CommandHandler('number', number)
dispatcher.add_handler(number_handler)

def email(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    
    bot.sendMessage(chat_id=update.message.chat_id,text="info@fiverr.com")
    bot.sendMessage(chat_id=update.message.chat_id, text= "Type /founder to find out who the founders of fiverr are \nType /history to get which year fiverr was founded \nType /noofusers to find out how many users currently use Fiverr \nType /location to find out the location of headquarters of Fiverr \nType /number to get Fiverr's corporate phone number\nType /email to get Fiverr's email")
      
email_handler = CommandHandler('email', email)
dispatcher.add_handler(email_handler)

#do command to clear all message 
#added last
def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")
    bot.sendMessage(chat_id=update.message.chat_id, text= "Type /founder to find out who the founders of fiverr are \nType /history to get which year fiverr was founded \nType /noofusers to find out how many users currently use Fiverr \nType /location to find out the location of headquarters of Fiverr \nType /number to get Fiverr's corporate phone number\nType /email to get Fiverr's email")
    
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

    
