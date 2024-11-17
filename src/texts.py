

class Content:
    set_lang = """Select language
Выберите язык
בחר שפה"""
    start_message = {
        "ru": """<b>Добро пожаловать</b>

Не знаем, как везде, но у нас с работой вседа все хорошо!)
На нашей платформе мы точно найдете себе достойную работу""",
        "en": """<b>Welcome</b>

We don't know how it works everywhere, but at our platform we have no problems with work)
On our platform, we will definitely find a job for you""",
        "he": """<b>ברוכים הבאים</b>
        
לא ידוע לנו מה קורה במקומות אחרים, אבל בפלטפורמה שלנו תמיד יש עבודה)
תמצא הת הקריירה הבאה שלך דרכינו!"""
    }
    work_list = {
        "ru": """<b>Список вакансий</b>
        
Выберите место работы, которое вас интересует""",
        "en": """<b>Work list</b>
        
Select the place of work you are interested in""",
        "he": """<b>רשימת משרות</b>
        
בחר את מקום עבודה המועדף עליך"""
    }
    work_panel = {
        "ru": """<b>{brand}</b>
        
<b><u>Описание: </u></b>{desc}

* Предусмотрен транспорт / оплата проезда
""",
        "en": """<b>{brand}</b>
        
<b><u>Description: </u></b>{desc}

* Transport / payment for travel
""",
        "he": """<b>{brand}</b>
        
<b><u>תיאור: </u></b>{desc}

* נסיעות / תשלום נסיעה
"""}
    work_all_details = {
        "ru": """<b>{brand}</b>
        
<b><u>Описание:</u></b> {desc}
<b><u>Время работы:</u></b>
{work_time}

<b><u>Подвозка:</u></b> {travel_expense_coverage}
<b><u>Требования:</u></b> 
{requirements}
<b><u>Город:</u></b> {city}
<b><u>Еда:</u></b> {food}""",
        "en": """<b>{brand}</b>
<b><u>Description:</u></b> {desc}
<b><u>Work time:</u></b>
{work_time}

<b><u>Transport:</u></b> {travel_expense_coverage}
<b><u>Requirements:</u></b> 
{requirements}
<b><u>City:</u></b> {city}
<b><u>Food:</u></b> {food}""",
        "he": """<b>{brand}</b>
<b><u>תיאור:</u></b> {desc}
<b><u>שעות עבודה:</u></b>
{work_time} 

<b><u>נסיעה:</u></b> {travel_expense_coverage}
<b><u>דרישות:</u></b> 
{requirements}
<b><u>עיר:</u></b> {city}
<b><u>אוכל:</u></b> {food}"""}
    work_submitted = {
        "ru": """Ваша заявка отправлена!""",
        "en": """Your application has been sent!""",
        "he": """הבקשה שלך נשלחה!"""
    }
    hour = {
        "ru": "час",
        "en": "hour",
        "he": "שעה"
    }
    requirements_required = {
        "ru": """Для использования онлайн заявок необходимо заполнить ваши личные данные в разделе "Профиль".""",
        "en": """To use online applications, you need to fill in your personal data in the "Profile" section.""",
        "he": """לקבלת שירותי אונליין יש למלא את הנתונים האישיים בפרופיל."""
    }
    profile = {
        "ru": """<b>Профиль</b>
        
<b><u>*Имя:</u></b> {name}
<b><u>*Документ:</u></b> {document}
<b><u>*Возраст:</u></b> {age}
<b><u>*Пол:</u></b> {sex}
<b><u>*Телефон:</u></b> {phone}
<b><u>Телефон 2:</u></b> {phone2}
<b><u>*Город:</u></b> {city}

Пункты обязательные для оформления онлайн заявок отмечены звездочкой""",
        "en": """<b>Profile</b>
        
<b><u>*Name:</u></b> {name}
<b><u>*Document:</u></b> {document}
<b><u>*Age:</u></b> {age}
<b><u>*Gender:</u></b> {sex}
<b><u>*Phone:</u></b> {phone}
<b><u>Phone 2:</u></b> {phone2}
<b><u>*City:</u></b> {city}

Points required for online applications are marked with a star""",
        "he": """<b>פרופיל</b>
        
<b><u>*שם:</u></b> {name}
<b><u>*תעודת זהות:</u></b> {document}
<b><u>*גיל:</u></b> {age}
<b><u>*מין:</u></b> {sex}
<b><u>*טלפון:</u></b> {phone}
<b><u>*טלפון 2:</u></b> {phone2}
<b><u>*עיר:</u></b> {city}

הפרטים הנדרשים לרישום אונליין מסומנים בכוכבית"""
    }
    worker_set_name = {
        "ru": "Введите имя",
        "en": "Enter name",
        "he": "הזן שם"
    }
    worker_set_age = {
        "ru": "Введите возраст",
        "en": "Enter age",
        "he": "הזן גיל"
    }
    worker_set_sex = {
        "ru": "Выберите пол",
        "en": "Select gender",
        "he": "בחר מין"
    }
    worker_set_phone = {
        "ru": "Введите номер телефона",
        "en": "Enter phone number",
        "he": "הזן מספר טלפון"
    }
    worker_set_phone2 = {
        "ru": "Введите номер телефона",
        "en": "Enter phone number",
        "he": "הזן מספר טלפון"
    }
    worker_set_document = {
        "ru": """Отправьте любое удостоверение личности. 
Это может быть загранпаспорт, синяя бумага, теудат зеут или водительское удостоверение.""",
        "en": """Send any identity document. 
This can be a passport, a blue card, a passport or a driver's license.""",
        "he": """שלחו את התעודת הזהות שלכם."""
    }
    worker_set_city = {
        "ru": "Введите город проживания",
        "en": "Enter city of residence",
        "he": "הזן עיר מגורים"
    }


class Button:
    en = {
        "ru": "🇬🇧 English",
        "en": "🇬🇧 English",
        "he": "🇬🇧 English"
    }
    ru = {
        "ru": "🇷🇺 Русский",
        "en": "🇷🇺 Русский",
        "he": "🇷🇺 Русский"
    }
    he = {
        "ru": "🇮🇱 עברית",
        "en": "עברית 🇮🇱",
        "he": "עברית 🇮🇱"
    }
    back = {
        "ru": "👈 Назад ",
        "en": "👈 Back",
        "he": "👈 חזרה"
    }
    user_language = {
        "ru": "🌐 Сменить язык",
        "en": "🌐 Change language",
        "he": "🌐 שנה שפה"
    }
    work_list = {
        "ru": "💼 Список вакансий",
        "en": "💼 Work list",
        "he": "💼 רשימת משרות"
    }
    work_payment = {
        "ru": "💸 Часы и ЗП",
        "en": "💸 Hours & Salary 💸",
        "he": "💸 שעות ושכר"
    }
    work_all_details = {
        "ru": "📝 Подробности",
        "en": "📝 Details",
        "he": "📝 פרטים"
    }
    submit_online = {
        "ru": "Подать заявку онлайн ",
        "en": "Submit online ",
        "he": "הצטרפות אונליין"
    }
    whatsapp = {
        "ru": "📲 WhatsApp",
        "en": "📲 WhatsApp",
        "he": "📲 WhatsApp"
    }
    phone = {
        "ru": "📞 Телефон ",
        "en": "📞 Phone",
        "he": "📞 טלפון"
    }
    profile = {
        "ru": "👤 Профиль",
        "en": "👤 Profile",
        "he": "👤 פרופיל"
    }
    submissions = {
        "ru": "📝 Заявки",
        "en": "📝 Submissions",
        "he": "📝 בקשות וטפסים"
    }
    accept = {
        "ru": "👍 Принять ",
        "en": "👍 Accept",
        "he": "👍 אשר"
    }
    reject = {
        "ru": "👎 Отклонить",
        "en": "👎 Reject",
        "he": "👎 דחה"
    }
    set_name = {
        "ru": "👤 Имя",
        "en": "👤 Name",
        "he": "👤 שם"
    }
    set_personal_id = {
        "ru": "📝 Удостоверение (любое) ",
        "en": "📝 Document (any)",
        "he": "📝 תעודת זהות (או רשיון)"
    }
    set_age = {
        "ru": "📆 Возраст",
        "en": "📆 Age",
        "he": "📆 גיל"
    }
    set_sex = {
        "ru": "👩‍👩‍👧‍👦 Пол",
        "en": "👩‍👩‍👧‍👦 Gender ",
        "he": "👩‍👩‍👧‍👦 מין"
    }
    set_phone = {
        "ru": "📞 Телефон ",
        "en": "📞 Phone",
        "he": "📞 טלפון"
    }
    set_phone2 = {
        "ru": "📞 Телефон 2",
        "en": "📞 Phone 2",
        "he": "📞 טלפון 2"
    }
    set_city = {
        "ru": "🏙️ Город ",
        "en": "🏙️ City",
        "he": "🏙️ עיר"
    }
    male = {
        "ru": "👨 Мужской ",
        "en": "👨 Male",
        "he": "👨 זכר"
    }
    female = {
        "ru": "👩 Женский",
        "en": "👩 Female",
        "he": "👩 נקבה"
    }
    group_on_my_lang = {
        "ru": "🇷🇺 Группа на Русском",
        "en": "🇬🇧 Group on English language",
        "he": "🇮🇱 קבוצה בעברית"
    }
    more_jobs = {
        "ru": "📝 Еще вакансии",
        "en": "📝 More jobs",
        "he": "📝 עוד משרות"
    }
    agent_on_telegram = {
        "ru": "👤 Связаться в Telegram",
        "en": "👤 Contact in Telegram",
        "he": "👤 צור קשר בטלגרם"
    }



