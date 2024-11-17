import random
import time

from src.connections import *
from src.models import *

groups = [
    {"id": "", "lang": "he"},
    {"id": "", "lang": "ru"},
    {"id": "", "lang": "en"}
]

ad_photo = {
    "24001": "AgACAgEAAxkBAANpZzkQay6RSyhIoVB0q0tSOReFXBgAAl2vMRsWIMlFxEb1lZ2lbukBAAMCAAN5AAM2BA",
    "24002": "AgACAgEAAxkBAANqZzkRAZHIfjEPz0tao2-hyhOAFmgAAl6vMRsWIMlFshW9umdjIYMBAAMCAAN5AAM2BA",
    "24003": "AgACAgEAAxkBAAN-Zzkap_sO-8RNYi6WMj-hYwaik2sAAmKvMRsWIMlFoHhu2v5cSF8BAAMCAAN5AAM2BA",
    "24004": "AgACAgEAAxkBAAN_ZzkateSKbev-lNK0j3_N7hj7THMAAmOvMRsWIMlFx4uvYIgKgkMBAAMCAAN5AAM2BA"
}

while True:
    for group in groups:

        for work in Work().get():
            if work.status == "show":
                work_id = work.work_id
                last_message_time = Post(group["id"]).last_message_time()

                if datetime.datetime.now() - last_message_time > datetime.timedelta(days=1):
                    Post(group["id"], work_id).add()

                    w = Work(work_id)
                    w.get()

                    if w.name == "Sano":
                        photo = "AgACAgEAAxkBAANpZzkQay6RSyhIoVB0q0tSOReFXBgAAl2vMRsWIMlFxEb1lZ2lbukBAAMCAAN5AAM2BA"
                    elif w.name == "H&M":
                        photo = "AgACAgEAAxkBAANqZzkRAZHIfjEPz0tao2-hyhOAFmgAAl6vMRsWIMlFshW9umdjIYMBAAMCAAN5AAM2BA"
                    elif w.name == "Castro":
                        photo = "AgACAgEAAxkBAAN-Zzkap_sO-8RNYi6WMj-hYwaik2sAAmKvMRsWIMlFoHhu2v5cSF8BAAMCAAN5AAM2BA"
                    elif w.name == "911 (Story)":
                        photo = "AgACAgEAAxkBAAN_ZzkateSKbev-lNK0j3_N7hj7THMAAmOvMRsWIMlFx4uvYIgKgkMBAAMCAAN5AAM2BA"
                    else:
                        photo = "None"

                    desc = str(eval(f"w.description_{group['lang']}"))
                    requirements = str(eval(f"w.requirements_{group['lang']}"))
                    city = str(eval(f"w.city_{group['lang']}"))

                    work_time = ""
                    if w.day_work_time != "None":
                        work_time += f"• {w.day_work_time} ({w.day_price_per_hour}/{texts.Content.hour[group['lang']]})\n"
                    if w.night_work_time != "None":
                        work_time += f"• {w.night_work_time} ({w.night_price_per_hour}/{texts.Content.hour[group['lang']]})"

                    k = kmarkup()
                    msg = texts.Content.work_all_details[group['lang']].format(**{
                        "brand": w.name,
                        "desc": desc,
                        "work_time": work_time,
                        "travel_expense_coverage": w.travel_expense_coverage,
                        "requirements": requirements,
                        "city": city,
                        "food": w.food,
                        "status": w.status
                    })

                    k.row(btn(texts.Button.whatsapp[group["lang"]], url=f"https://wa.me/972504834744"),
                          btn(texts.Button.more_jobs[group["lang"]], url=f"https://t.me/MorLogisticsBot"))
                    k.row(btn(texts.Button.agent_on_telegram[group["lang"]], url=f"https://t.me/MorLogistics"))
                    bot.send_photo(group["id"], photo, caption=work.description, reply_markup=k)

                    print("[+]", "Post sent:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    print("[+]", "Group:", group["id"])
                    print("[+]", "Work:", w.work_id, w.name)

                    time.sleep(10)




