import datetime
import random
import time, os
from src.connections import *
from src.models import *

# os.chdir("/home/promiteus/Desktop/mpb_poster")

groups = [
    {"id": -1001300356812, "lang": "he"},
    {"id": -1001334146855, "lang": "ru"},
    {"id": -1001388700521, "lang": "en"}
]


def pick(filename, data):
    import pickle

    with open(filename, "wb") as f:
        pickle.dump(data, f)


def unpick(filename):
    import pickle

    with open(filename, "rb") as f:
        return pickle.load(f)


work_num = 0
groups_num = 0
while True:
    for work in Work().get():
        work_num += 1
        for group in groups:
            groups_num += 1
            if work.status == "show":
                def sender():
                    try:
                        work_id = work.work_id
                        # last_message_time = Post(group["id"]).last_message_time()

                        Post(group["id"], work_id).add()

                        if work.name == "Sano":
                            photo = "AgACAgEAAxkBAANpZzkQay6RSyhIoVB0q0tSOReFXBgAAl2vMRsWIMlFxEb1lZ2lbukBAAMCAAN5AAM2BA"
                        elif work.name == "H&M":
                            photo = "AgACAgEAAxkBAANqZzkRAZHIfjEPz0tao2-hyhOAFmgAAl6vMRsWIMlFshW9umdjIYMBAAMCAAN5AAM2BA"
                        elif work.name == "Castro":
                            photo = "AgACAgEAAxkBAAN-Zzkap_sO-8RNYi6WMj-hYwaik2sAAmKvMRsWIMlFoHhu2v5cSF8BAAMCAAN5AAM2BA"
                        elif work.name == "911 (Story)":
                            photo = "AgACAgEAAxkBAAN_ZzkateSKbev-lNK0j3_N7hj7THMAAmOvMRsWIMlFx4uvYIgKgkMBAAMCAAN5AAM2BA"
                        else:
                            photo = "None"

                        desc = str(eval(f"work.description_{group['lang']}"))
                        requirements = str(eval(f"work.requirements_{group['lang']}"))
                        city = str(eval(f"work.city_{group['lang']}"))

                        work_time = ""
                        if work.day_work_time != "None":
                            work_time += f"• {work.day_work_time} ({work.day_price_per_hour}/{texts.Content.hour[group['lang']]})\n"
                        if work.night_work_time != "None":
                            work_time += f"• {work.night_work_time} ({work.night_price_per_hour}/{texts.Content.hour[group['lang']]})"

                        k = kmarkup()
                        msg = texts.Content.work_all_details[group['lang']].format(**{
                            "brand": work.name,
                            "desc": desc,
                            "work_time": work_time,
                            "travel_expense_coverage": work.travel_expense_coverage,
                            "requirements": requirements,
                            "city": city,
                            "food": work.food,
                            "status": work.status
                        })

                        k.row(btn(texts.Button.whatsapp[group["lang"]], url=f"https://wa.me/972504834744"),
                              btn(texts.Button.more_jobs[group["lang"]], url=f"https://t.me/MorLogisticsBot"))
                        k.row(btn(texts.Button.agent_on_telegram[group["lang"]], url=f"https://t.me/MorLogistics"))
                        bot.send_photo(group["id"], photo, caption=msg, reply_markup=k, disable_notification=True)

                        print("[+]", "Post sent:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                        print("[+]", "Group:", group["id"])
                        print("[+]", "Work:", work.work_id, work.name)
                        print()
                    except Exception as e:
                        print("[+]", e)
                        print("[+]", "Sleeping for 20 seconds...")
                        time.sleep(20)
                        sender()

                sender()
        pick("src/d11", work.work_id)
        sleep_time = random.randint(60*60*4, 60*60*12)
        print("[+]", "Sleeping for:", str(datetime.timedelta(seconds=sleep_time)), " (" + str(datetime.datetime.now() + datetime.timedelta(seconds=sleep_time)) + ")")
        time.sleep(sleep_time)




