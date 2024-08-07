"""wallpy is a telegram bot"""
import os
from telegram.ext import *
from dotenv import load_dotenv
import commands
import reminder
import responses
import datetime

load_dotenv()
API_KEY = os.environ["API_KEY"]

print("starting up bot")


def handler(update,context):
    res = responses.msg_hndler(update.message.text)
    update.message.reply_text(res)



def error_handler(update,context):
    print (f"update {update} caused {context.error}")
    raise context.error

def main():
    updater = Updater(API_KEY, use_context = True)
    dp = updater.dispatcher
    job_queue = updater.job_queue
    job_queue.run_daily(reminder.remindme, days=(0, 1, 2, 3, 4, 5, 6), time=datetime.time(hour=15, minute=59, second=00))
    job_queue.start()

    dp.add_handler(CommandHandler('start',commands.start_command))

    dp.add_handler(CommandHandler('help', commands.help_command))
    dp.add_handler(CommandHandler('custom', commands.custom_command))
    dp.add_handler(CommandHandler('wallpaper', commands.wallpaper_command))
    dp.add_handler(CommandHandler('gif',commands.gif_command))
    dp.add_handler(CommandHandler('reminder',commands.reminder_command))

    dp.add_handler(MessageHandler(Filters.text,handler))

    dp.add_error_handler(error_handler)

    updater.start_polling()
    updater.idle()

main()

