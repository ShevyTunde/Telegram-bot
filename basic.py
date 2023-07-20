import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Replace 'YOUR_API_TOKEN' with the API token you received from the BotFather
API_TOKEN = 'YOUR_API_TOKEN'

# Create an Updater object to receive updates from Telegram
updater = Updater(API_TOKEN)

# Create a dispatcher to register handlers
dispatcher = updater.dispatcher

# Define a command handler to handle the /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am your Echo Bot.')

# Define a command handler to handle the /help command
def help(update: Update, context: CallbackContext):
    update.message.reply_text('You can send me any message, and I will echo it back to you!')

# Define a message handler to handle all text messages
def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

# Register the handlers with the dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Start the bot
updater.start_polling()

# Run the bot until you press Ctrl-C to stop it
updater.idle()
