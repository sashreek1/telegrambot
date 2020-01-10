import logging
import requests
from telegram.ext import Updater, CommandHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('Hi!, run /help to view the commands')


def help(update, context):
    update.message.reply_text('run /numbers to get the number forks of the fedora-infra repository along with each project\'s specific count ')


def numbers (update,context):
    r = requests.get('https://api.github.com/orgs/fedora-infra/repos').json()
    num = 0
    for i in range(len(r)):
        num += r[i]['forks']
        update.message.reply_text(r[i]['name']+" : "+str(r[i]['forks']))
    update.message.reply_text('total number of forks are :'+str(num))


def main_func():
    updater = Updater("TOKEN", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("numbers", numbers))
    updater.start_polling()
    updater.idle()


main_func()
