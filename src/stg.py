import datetime

from src.connections import *
from src import texts, models
from src.models import UserLanguage, get_button, get_content


def start_message(chat_id):
    models.Sub(chat_id).update()
    w = models.Worker(chat_id)
    if not w.get():
        w.status = "pending"
        w.reg_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        w.start_date = "None"
        w.insert()

    k = kmarkup()
    msg = get_content(chat_id, "start_message")
    k.row(btn(get_button(chat_id, "group_on_my_lang"), url=f"https://t.me/MorLogistics_{UserLanguage(chat_id).get()}"))
    k.row(btn(get_button(chat_id, "work_list"), callback_data="work_list"))
    k.row(btn(get_button(chat_id, "profile"), callback_data="profile"),
          btn(get_button(chat_id, "user_language"), callback_data="user_language"))
    bot.send_message(chat_id, msg, reply_markup=k)

    models.Stage(chat_id).set("None")


def user_language(chat_id):
    k = kmarkup()
    k.row(btn(get_button(chat_id, "en"), callback_data="user_language||en"),
          btn(get_button(chat_id, "ru"), callback_data="user_language||ru"))
    k.row(btn(get_button(chat_id, "he"), callback_data="user_language||he"))
    bot.send_message(chat_id, texts.Content.set_lang, reply_markup=k)


def work_list(chat_id):
    k = kmarkup()
    msg = get_content(chat_id, "work_list")

    for work in models.Work().get():
        k.row(btn(work.name, callback_data=f"work_panel||{work.work_id}"))
    k.row(models.back_btn(chat_id, "home"))
    bot.send_message(chat_id, msg, reply_markup=k)


def work_panel(chat_id, work_id):
    lng = UserLanguage(chat_id).get()
    w = models.Work(work_id)
    w.get()

    desc = str(eval(f"w.description_{lng}"))

    k = kmarkup()
    msg = get_content(chat_id, "work_panel").format(**{
        "brand": w.name,
        "desc": desc
    })

    k.row(btn(get_button(chat_id, "work_all_details"), callback_data=f"work_all_details||{work_id}"))
    # btn(get_button(chat_id, "work_payment"), callback_data=f"work_payment||{work_id}"))
    k.row(btn(get_button(chat_id, "submit_online"), callback_data=f"work_submit||{work_id}"))
    k.row(btn(get_button(chat_id, "whatsapp"), url=f"https://wa.me/972504834744"))

    if w.name == "Sano":
        photo = "AgACAgEAAxkBAANpZzkQay6RSyhIoVB0q0tSOReFXBgAAl2vMRsWIMlFxEb1lZ2lbukBAAMCAAN5AAM2BA"
    elif w.name == "H&M":
        photo = "AgACAgEAAxkBAANqZzkRAZHIfjEPz0tao2-hyhOAFmgAAl6vMRsWIMlFshW9umdjIYMBAAMCAAN5AAM2BA"
    elif w.name == "Castro":
        photo = "AgACAgEAAxkBAAN-Zzkap_sO-8RNYi6WMj-hYwaik2sAAmKvMRsWIMlFoHhu2v5cSF8BAAMCAAN5AAM2BA"
    elif w.name == "911 (Story)":
        photo = "AgACAgEAAxkBAAN_ZzkateSKbev-lNK0j3_N7hj7THMAAmOvMRsWIMlFx4uvYIgKgkMBAAMCAAN5AAM2BA"
    else:
        photo = None

    k.row(models.back_btn(chat_id, "work_list"))
    bot.send_photo(chat_id, photo=photo, caption=msg, reply_markup=k)


def work_all_details(chat_id, work_id):
    lng = UserLanguage(chat_id).get()
    w = models.Work(work_id)
    w.get()

    desc = str(eval(f"w.description_{lng}"))
    requirements = str(eval(f"w.requirements_{lng}"))
    city = str(eval(f"w.city_{lng}"))

    work_time = ""
    if w.day_work_time != "None":
        work_time += f"• {w.day_work_time} ({w.day_price_per_hour}/{get_content(chat_id, 'hour')})\n"
    if w.night_work_time != "None":
        work_time += f"• {w.night_work_time} ({w.night_price_per_hour}/{get_content(chat_id, 'hour')})"

    k = kmarkup()
    msg = get_content(chat_id, "work_all_details").format(**{
        "brand": w.name,
        "desc": desc,
        "work_time": work_time,
        "travel_expense_coverage": w.travel_expense_coverage,
        "requirements": requirements,
        "city": city,
        "food": w.food,
        "status": w.status
    })

    k.row(models.back_btn(chat_id, f"work_panel||{str(work_id)}"))
    bot.send_message(chat_id, msg, reply_markup=k)


def work_payment(call, work_id):
    w = models.Work(work_id)
    w.get()

    work_time = get_button(call.message.chat.id, "work_payment") + "\n\n"
    if w.day_work_time != "None":
        work_time += f"• {w.day_work_time} ({w.day_price_per_hour}/{get_content(call.message.chat.id, 'hour')})\n"
    if w.night_work_time != "None":
        work_time += f"• {w.night_work_time} ({w.night_price_per_hour}/{get_content(call.message.chat.id, 'hour')})\n"

    bot.answer_callback_query(call.id, work_time, show_alert=True)


def work_submit(chat_id, work_id):
    w = models.Worker(chat_id)
    worker_data = w.get()
    for i in ["name", "personal_id", "age", "sex", "phone", "phone2", "city", "work_id", "start_date", "reg_date", "status"]:
        if eval(f"worker_data.{i}") == "None":
            exec(f"worker_data.{i} = None")

    if all((worker_data.name, worker_data.personal_id, worker_data.age, worker_data.sex, worker_data.phone,
            worker_data.city, worker_data.status)):
        s = models.Submission(chat_id)
        s.work_id = work_id
        s.status = "pending"
        s.date_of_submission = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        s.insert()


        k = kmarkup()
        msg = "New work submission!"
        k.row(btn(get_button(chat_id, "submissions"), callback_data=f"admin_submissions"))
        bot.send_message(ADMIN_ID, msg, reply_markup=k)

        k = kmarkup()
        msg = get_content(chat_id, "work_submitted")
        k.row(models.back_btn(chat_id, f"work_panel||{str(work_id)}"))
        bot.send_message(chat_id, msg, reply_markup=k)


    else:
        k = kmarkup()
        msg = get_content(chat_id, "requirements_required")
        k.row(btn(get_button(chat_id, "profile"), callback_data=f"profile"))
        k.row(models.back_btn(chat_id, f"work_panel||{str(work_id)}"))
        bot.send_message(chat_id, msg, reply_markup=k)


def admin_submissions(chat_id):
    k = kmarkup()

    for submission in models.Submission().get():
        if submission.status == "pending":
            worker = models.Worker(submission.user_id)
            worker.get()
            k.row(btn(f"{worker.name} [{worker.user_id}]", callback_data=f"admin_submission_panel||{str(submission.user_id)}"))
    msg = "Submissions"
    bot.send_message(chat_id, msg, reply_markup=k)


def admin_submission_panel(chat_id, submission_id):
    k = kmarkup()
    submission = models.Submission(submission_id).get()
    worker = models.Worker(submission.user_id).get()
    work = models.Work(submission.work_id).get()

    msg = f"""{worker.name} [{worker.user_id}]

Work: {work.name}
Worker name: {worker.name}
Age: {worker.age}
Gender: {worker.sex}
City: {worker.city}
Phone: {worker.phone}
Submission date: {submission.date_of_submission}

"""
    k.row(btn(get_button(chat_id, "accept"), callback_data=f"admin_accept_submission||{str(submission_id)}"),
          btn(get_button(chat_id, "reject"), callback_data=f"admin_reject_submission||{str(submission_id)}"))

    bot.send_photo(chat_id, worker.personal_id, caption=msg, reply_markup=k)


def admin_accept_submission(chat_id, submission_id):
    s = models.Submission(submission_id)
    s.update(column="status", value="accepted")

    worker = models.Worker(s.user_id)
    if worker.get():
        worker.update(column="status", value="have_a_job")
        worker.update(column="work_id", value=s.work_id)

    admin_submissions(chat_id)


def admin_reject_submission(chat_id, submission_id):
    s = models.Submission(submission_id)
    s.delete()

    admin_submissions(chat_id)


def profile(chat_id):
    w = models.Worker(chat_id).get()
    p_id = "👎"
    gender = {
        "male": "👨",
        "female": "👩",
        "None": "👤"
    }

    if w.personal_id not in ["None", None]:
        p_id = "👍"

    k = kmarkup()
    msg = get_content(chat_id, "profile").format(**{
        "name": w.name,
        "document": p_id,
        "age": w.age,
        "sex": gender[w.sex],
        "phone": w.phone,
        "phone2": w.phone2,
        "city": w.city
    })

    k.row(btn(get_button(chat_id, "set_name"), callback_data=f"worker_set_name"),
          btn(get_button(chat_id, "set_personal_id"), callback_data=f"worker_set_personal_id"))
    k.row(btn(get_button(chat_id, "set_age"), callback_data=f"worker_set_age"),
          btn(get_button(chat_id, "set_sex"), callback_data=f"worker_set_sex"))
    k.row(btn(get_button(chat_id, "set_phone"), callback_data=f"worker_set_phone"),
          btn(get_button(chat_id, "set_phone2"), callback_data=f"worker_set_phone2"))
    k.row(btn(get_button(chat_id, "set_city"), callback_data=f"worker_set_city"))

    k.row(models.back_btn(chat_id, "home"))

    bot.send_message(chat_id, msg, reply_markup=k)
    models.Stage(chat_id).set("None")


def worker_set_name(chat_id, name=None):
    if name:
        w = models.Worker(chat_id)
        w.update(column="name", value=name)
    else:
        k = kmarkup()
        msg = get_content(chat_id, "worker_set_name")
        k.row(models.back_btn(chat_id, "profile"))
        bot.send_message(chat_id, msg, reply_markup=k)

        models.Stage(chat_id).set("worker_set_name")


def worker_set_personal_id(chat_id, personal_id=None):
    if personal_id:
        w = models.Worker(chat_id)
        w.update(column="personal_id", value=personal_id)
    else:
        k = kmarkup()
        msg = get_content(chat_id, "worker_set_document")
        k.row(models.back_btn(chat_id, "profile"))
        bot.send_message(chat_id, msg, reply_markup=k)

        models.Stage(chat_id).set("worker_set_personal_id")


def worker_set_age(chat_id, age=None):
    if age:
        w = models.Worker(chat_id)
        w.update(column="age", value=age)
    else:
        k = kmarkup()
        msg = get_content(chat_id, "worker_set_age")
        k.row(models.back_btn(chat_id, "profile"))
        bot.send_message(chat_id, msg, reply_markup=k)

        models.Stage(chat_id).set("worker_set_age")


def worker_set_sex(chat_id, sex=None):
    if sex:
        w = models.Worker(chat_id)
        w.update(column="sex", value=sex)
    else:
        k = kmarkup()
        msg = get_content(chat_id, "worker_set_sex")
        k.row(btn(get_button(chat_id, "male"), callback_data=f"worker_set_sex||male"),
              btn(get_button(chat_id, "female"), callback_data=f"worker_set_sex||female"))
        k.row(models.back_btn(chat_id, "profile"))
        bot.send_message(chat_id, msg, reply_markup=k)


def worker_set_phone(chat_id, phone=None):
    if phone:
        w = models.Worker(chat_id)
        w.update(column="phone", value=phone)
    else:
        k = kmarkup()
        msg = get_content(chat_id, "worker_set_phone")
        k.row(models.back_btn(chat_id, "profile"))
        bot.send_message(chat_id, msg, reply_markup=k)

        models.Stage(chat_id).set("worker_set_phone")


def worker_set_phone2(chat_id, phone2=None):
    if phone2:
        w = models.Worker(chat_id)
        w.update(column="phone2", value=phone2)
    else:
        k = kmarkup()
        msg = get_content(chat_id, "worker_set_phone2")
        k.row(models.back_btn(chat_id, "profile"))
        bot.send_message(chat_id, msg, reply_markup=k)

        models.Stage(chat_id).set("worker_set_phone2")


def worker_set_city(chat_id, city=None):
    if city:
        w = models.Worker(chat_id)
        w.update(column="city", value=city)
    else:
        k = kmarkup()
        msg = get_content(chat_id, "worker_set_city")
        k.row(models.back_btn(chat_id, "profile"))
        bot.send_message(chat_id, msg, reply_markup=k)

        models.Stage(chat_id).set("worker_set_city")


