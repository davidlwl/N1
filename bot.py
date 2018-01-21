from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove,ChatAction)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

GENDER,BIO,PHOTO,LOCATION = range(4)

def start(bot, update):
    reply_keyboard = [['кошка', 'собака', 'другое']]

    update.message.reply_text(
        'Выберите вашего питомца',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return GENDER

def animal(bot, update):
    user = update.message.from_user
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    update.message.reply_text('Вам нужна ветпомощь на дому?')
    reply_keyboard = [['да, срочно', 'да, скоро','пока нет']]

    update.message.reply_text(
        'Вам нужна ветпомощь на дому?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return BIO
    
def homevisit(bot, update):
    user = update.message.from_user
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    if update.message.text == 'да, срочно' or 'да, скоро':
        update.message.reply_text('8 (499) 110-01-05')
    elif update.message.text == 'пока нет':
        update.message.reply_text('Мы в соц.сетях: подпишитесь”: http://www.veterinardoma.ru/vetklinika-socialniye-seti.php')
    
    reply_keyboard = [['да', 'нет']]
    update.message.reply_text(
        'Вам нужна консультация онлайн?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return PHOTO

def consultation(bot, update):
    user = update.message.from_user
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    if update.message.text == 'да':
        update.message.reply_text('http://www.veterinardoma.ru/veterinary_voprosy.php')
    elif update.message.text == 'нет':
        update.message.reply_text('“Отзывы”: '+'http://www.veterinardoma.ru/otzivy_vet.php')
    
    reply_keyboard = [['статьи', 'ответы ветеринара', 'подпшитесь на нашу рассылку']]

    update.message.reply_text(
        'Ознакомьтесь',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return LOCATION
 
def read(bot, update):
    user = update.message.from_user
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    if update.message.text == 'статьи':
        update.message.reply_text('http://www.veterinardoma.ru/veterinaria.htm')
    elif update.message.text == 'ответы ветеринара':
        update.message.reply_text('http://www.veterinardoma.ru/veterinar-voprosy-otvety2.php')
    elif update.message.text == 'подпшитесь на нашу рассылку':
        update.message.reply_text('http://www.veterinardoma.ru/rassilka-veterinarnaya-pomosh.php')
    update.message.reply_text('Press /start again to view options!')

    
def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the EventHandler and pass it your bot's token.
    #updater = Updater("525002581:AAFCaGvfaDIRdz938J--Bb83SPmn20V--Yo")
    updater = Updater("521629190:AAHMEmlRRuq29_8hbr6uui1tCGXImo_GOmQ")
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            GENDER: [RegexHandler('^(кошка|собака|другое)$', animal)],
            BIO: [RegexHandler('^(да, срочно|да, скоро|пока нет)$', homevisit)],
            PHOTO: [RegexHandler('^(да|нет)$', consultation)],
            LOCATION: [RegexHandler('^(статьи|ответы ветеринара|подпшитесь на нашу рассылку)$', read)],
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    


while True:
  main()


    
