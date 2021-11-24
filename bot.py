"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import telegram
import os
import sys
import requests
import urllib.request




import bot
from telegram.ext import ConversationHandler


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TXT, NAMER, VOICE, IMG = range(4)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')
    update.message.reply_text('I Am Online')
    update.message.reply_text('This Bot Was Made By @g4_media')
    update.message.reply_text('Please Consider Subscribing our Youtube Channel https://www.youtube.com/channel/UCad4U0t57KqjvHxqqdmZW_w')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')
    update.message.reply_text("This is a Multi Function Bot\nThis Bot was Made By @g4_media\n\nThis Bot Can Rename Files Upto 100MB\n	For This you Have to send the document to this bot\n	And provide new name whwn asked\n\nThis Bot Can Convert Voice Messege to audio file and audio document\n	For this you Have to send the voice message to this bot\n	And provide filename with disired filetype extention\n	eg : music.mp3\n	You will get the voice message as audio file and audio document\n\nThis Bot Can Convert Audio file to voice message\n	For this you have to send the audio file to ths bot\n	And you will get the audio file as voice message\n\nThis Bot Can Clear Captions of image\n	Just Send the image \n	You will get the Image as caption cleared")
    
def fuck(update, context):
    """Send a message when the command /fuck is issued."""
    update.message.reply_text('come lets do sex!')

def hai(update, context):
    """Send a message when the command /hai is issued."""
    update.message.reply_text('hello how are you')

def photo_handler(update, context):
    global fileid
    fileid = file_id = update.message.photo[-1].file_id
    img = 'AgACAgUAAxkBAAPhYY_0PJPm26fFXI1CY16m3lzbxFEAAqytMRuuy3lUA0If8V2l7rYBAAMCAAN5AAMiBA'
    pic='t_logo.png'
        
        
    update.message.reply_photo(update.message.photo[-1])
        
    print (fileid)
    update.message.reply_text("Please Enter Name For image File with Desired Extention ")
        
    return IMG

def file_handler(update, context):
    update.message.reply_text(update.message.document.file_name)
    update.message.reply_text(update.message.document.mime_type)
    update.message.reply_text(update.message.document.file_id)
    update.message.reply_text("I Recognied This as a document ")
    print (update.message.document.file_name)
        
        
    global filesname
    fileid = update.message.document.file_id
    filesname = update.message.document.file_name
    file = context.bot.getFile(fileid)
    file.download(filesname)
    update.message.reply_text(update.message.document.file_name)
        
    context.bot.sendDocument(chat_id=update.effective_chat.id, document=open(filesname, 'rb'), filename=filesname)
    if update.message.document.mime_type == "image/jpeg" or update.message.document.mime_type == "image/png" :
       update.message.reply_text("Hey this is an image file")
       context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(filesname,'rb'))
       return ConversationHandler.END

def imgup(update, context):
   update.message.reply_text("OK")
   fln=update.message.text
 
   if fln == "/restart" :
      python = sys.executable
      os.execl(python, python, * sys.argv)
   elif fln == "/cancel" :
        update.message.reply_text("Current Operation Canceled")
        return ConversationHandler.END
             
   global file
           
           
   file = context.bot.getFile(fileid)
   file.download(fln)
   update.message.reply_text(fln)
   
           
   context.bot.sendDocument(chat_id=update.effective_chat.id, document=open(fln, 'rb'), filename=fln)
           
   os.remove(fln)
   update.message.reply_text("Thank You Have A Nice Day")
   update.message.reply_text('This Bot Was Made By @g4_media')
   update.message.reply_text('Please Consider Subscribing our Youtube Channel https://www.youtube.com/channel/UCad4U0t57KqjvHxqqdmZW_w')
   return ConversationHandler.END


def text(update, context):
    mesg=update.message.text
    fp = urllib.request.urlopen(mesg)
    ext=fp.geturl()
    print(ext)
    start = 'https://www.youtube.com/watch?v='
    end = '&feature=youtu.be'
    print('\n')
    sol=str((ext.split(start))[1].split(end)[0])
    mes = "https://img.youtube.com/vi/"+sol+"/maxresdefault.jpg"
    print(mes)
    
    global filesname
    if "http" in mes: 
         def is_downloadable(url):
             """
             Does the url contain a downloadable resource
             """
             h = requests.head(url, allow_redirects=True)
             header = h.headers
             content_type = header.get('content-type')
             if 'text' in content_type.lower():
                 return False
             if 'html' in content_type.lower():
                 return False
             return True
         if str(is_downloadable(mes)):
            update.message.reply_text("Hey it is an Downloadable Link")
            if mes.find('/'):
               filename=mes.rsplit('/', 1)[1]
               filesname=filename[-10:]
               url = mes
               r = requests.get(url, allow_redirects=True, headers = {'User-agent': 'your bot 0.1'})

               open(filesname, 'wb').write(r.content)
               update.message.reply_text("Please enter a file name with extension")
               return TXT
              
def urlup(update, context):
    mes = update.message.text
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(filesname,'rb'))
    context.bot.sendDocument(chat_id=update.effective_chat.id, document=open(filesname, 'rb'), filename=mes)
    os.remove(filesname)
    return ConversationHandler.END



def error(update, context):
   """Log Errors caused by Updates."""
   logger.warning('Update "%s" caused error "%s"', update, context.error)
   update.message.reply_text("Sorry Error Occured   " + str(context.error))
   
def cancel(update, context):
   update.message.reply_text("Current Operation Canceled")
   os.remove(filesname)
   return ConversationHandler.END
   
   
def main():
   """Start the bot."""
   # Create the Updater and pass it your bot's token.
   # Make sure to set use_context=True to use the new context based callbacks
   # Post version 12 this will no longer be necessary
   updater = Updater(os.environ['bottoken'], use_context=True)

   # Get the dispatcher to register handlers
   dp = updater.dispatcher

   # on different commands - answer in Telegram
   dp.add_handler(CommandHandler("start", start))
   dp.add_handler(CommandHandler("help", help))
   dp.add_handler(CommandHandler("fuck", fuck))
   dp.add_handler(CommandHandler("hai", hai))

   # on noncommand i.e message - echo the message on Telegram
   # dp.add_handler(MessageHandler(Filters.text, echo))
   # dp.add_handler(MessageHandler(Filters.photo, photo_handler))
   dp.add_handler(MessageHandler(Filters.document, file_handler))
   # dp.add_handler(MessageHandler(Filters.all, admin_handler))

   conc_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.photo, photo_handler)],
        states={
            
            IMG: [MessageHandler(Filters.text, imgup)]
            
        },
        fallbacks=[MessageHandler(Filters.command, cancel)],
    )
 
   dp.add_handler(conc_handler)
  
   text_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text, text)],
        states={
            
            TXT: [MessageHandler(Filters.text, urlup)]
            
        },
        fallbacks=[MessageHandler(Filters.command, cancel)],
    )
 
   dp.add_handler(text_handler)

    # log all errors
   dp.add_error_handler(error)

    # Start the Bot
   updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
   updater.idle()

if __name__ == '__main__':
   main()
