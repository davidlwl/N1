from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove,ChatAction)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
import telegram
import logging

bot = telegram.Bot(token='524482039:AAFIx91svJA57QMI9Eqj3mifZRvBAuqdJm4')
updater = Updater("524482039:AAFIx91svJA57QMI9Eqj3mifZRvBAuqdJm4")
# Get the dispatcher to register handlers
dp = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater.start_polling()


GENDER,BIO,PHOTO,LOCATION,FINAL,FINAL2 = range(6)

def start(bot, update):
    reply_keyboard = [['cat', 'dog', 'others']]

    update.message.reply_text(
        'What kind of animal do you have?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return GENDER

def animal(bot, update):
    user = update.message.from_user
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    reply_keyboard = [['yes, right away', 'yes, later','not now']]

    update.message.reply_text(
        'Do you need a homevisit?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return BIO
    
def homevisit(bot, update):
    user = update.message.from_user
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    if update.message.text == 'yes, right away' or 'yes, later':
        update.message.reply_text('Please call: 8 (499) 110-01-05')
    elif update.message.text == 'not now':
        update.message.reply_text('Please visit: http://www.veterinardoma.ru/vetklinika-socialniye-seti.php')
    
    reply_keyboard = [['yes', 'no']]
    update.message.reply_text(
        'Do you need a consultation?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return PHOTO

def consultation(bot, update):
    user = update.message.from_user
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    if update.message.text == 'yes':
        update.message.reply_text('http://www.veterinardoma.ru/veterinary_voprosy.php')
    elif update.message.text == 'no':
        update.message.reply_text('http://www.veterinardoma.ru/otzivy_vet.php')
    
    reply_keyboard = [['articles', 'Q&A', 'subscribe to our newsletter']]

    update.message.reply_text(
        'Please Read: ',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return LOCATION
 
def read(bot, update):
    user = update.message.from_user
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    if update.message.text == 'articles':
        update.message.reply_text('http://www.veterinardoma.ru/veterinaria.htm')
    elif update.message.text == 'Q&A':
        update.message.reply_text('http://www.veterinardoma.ru/veterinar-voprosy-otvety2.php')
    elif update.message.text == 'subscribe to our newsletter':
        update.message.reply_text('http://www.veterinardoma.ru/rassilka-veterinarnaya-pomosh.php')
    
    reply_keyboard = [['Click here for a 100 р discount!']]
    update.message.reply_text(
        '------------------------------',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
    return FINAL

def final(bot, update):
    user = update.message.from_user
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    if update.message.text == 'Click here for a 100 р discount!':
        reply_keyboard = [['Subscribe to VK']]
    update.message.reply_text(
        'Discount Code: 2018vet',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
       
    return FINAL2

def final2(bot, update):
    user = update.message.from_user
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    if update.message.text == 'Subscribe to VK':
        update.message.reply_text('https://vk.com/vetclinicvasilek')
        
    return ConversationHandler.END
    
def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


# Create the EventHandler and pass it your bot's token.
#updater = Updater("525002581:AAFCaGvfaDIRdz938J--Bb83SPmn20V--Yo")


# Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],

    states={
        GENDER: [RegexHandler('^(cat|dog|others)$', animal)],
        BIO: [RegexHandler('^(yes, right away|yes, later|not now)$', homevisit)],
        PHOTO: [RegexHandler('^(yes|no)$', consultation)],
        LOCATION: [RegexHandler('^(articles|Q&A|subscribe to our newsletter)$', read)],
        FINAL: [RegexHandler('^(|Click here for a 100 р discount!)$', final)],
        FINAL2: [RegexHandler('^(|Subscribe to VK|)$', final2)]
    },

    fallbacks=[CommandHandler('cancel', cancel)]
)

dp.add_handler(conv_handler)


    



    
