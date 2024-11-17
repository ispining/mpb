import threading
import time

from src.connections import *
from src import texts, stg, models
from src.models import UserLanguage, get_button, get_content


@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    if message.chat.type == "private":
        if UserLanguage(chat_id).get() == None:
            stg.user_language(chat_id)
        else:
            stg.start_message(chat_id)


@bot.message_handler(content_types=['photo'])
def photo_message(message):
    chat_id = message.chat.id
    file_id = message.photo[-1].file_id

    cd = models.Stage(chat_id).get().split("||")

    if message.chat.type == "private":
        print(file_id)
        if cd[0] == "worker_set_personal_id":
            stg.worker_set_personal_id(chat_id, file_id)
            stg.profile(chat_id)


@bot.message_handler(commands=["panel"])
def panel_message(message):
    chat_id = message.chat.id
    if message.chat.type == "private":
        stg.admin_submissions(chat_id)


@bot.message_handler(content_types=['text'])
def text_message(message):
    chat_id = message.chat.id
    cd = models.Stage(chat_id).get().split("||")
    if message.chat.type == "private":
        if cd[0].startswith("worker_set_"):
            exec(f"stg.{cd[0]}(chat_id, message.text)")
            stg.profile(chat_id)
            models.Stage(chat_id).set("None")


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    cd = call.data.split("||")

    def dm():
        try:
            bot.delete_message(chat_id, call.message.message_id)
        except:
            pass

    if cd[0] == "home":
        stg.start_message(chat_id)
        dm()

    elif cd[0] == "user_language":
        if len(cd) == 1:
            stg.user_language(chat_id)
        else:
            UserLanguage(chat_id).set(cd[1])
            stg.start_message(chat_id)
        dm()

    elif cd[0] == "work_list":
        stg.work_list(chat_id)
        dm()

    elif cd[0] == "work_panel":
        work_id = cd[1]
        stg.work_panel(chat_id, work_id)
        dm()

    elif cd[0] == "work_all_details":
        work_id = cd[1]
        stg.work_all_details(chat_id, work_id)
        dm()

    elif cd[0] == "work_payment":
        work_id = cd[1]
        stg.work_payment(call, work_id)

    elif cd[0] == "work_submit":
        work_id = cd[1]
        stg.work_submit(chat_id, work_id)
        dm()

    elif cd[0] == "admin_submissions":
        stg.admin_submissions(chat_id)
        dm()

    elif cd[0] == "admin_submission_panel":
        submission_id = cd[1]
        stg.admin_submission_panel(chat_id, submission_id)
        dm()

    elif cd[0] == "admin_accept_submission":
        submission_id = cd[1]
        stg.admin_accept_submission(chat_id, submission_id)
        dm()

    elif cd[0] == "profile":
        stg.profile(chat_id)
        dm()

    elif cd[0] == "worker_set_sex":
        if len(cd) == 1:
            stg.worker_set_sex(chat_id)
        else:
            stg.worker_set_sex(chat_id, cd[1])
            stg.profile(chat_id)
        dm()

    elif cd[0].startswith("worker_set_"):
        exec(f"stg.{cd[0]}(chat_id)")
        dm()


def run():
    while True:
        try:
            bot.polling()
        except Exception as e:
            print(e)


def main():
    threading.Thread(target=run, daemon=True).start()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break


main()