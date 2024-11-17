from src.connections import Database, btn, DEBUG
from src import texts
import datetime


def prepare_db():
    with Database() as (db, sql):
        def user_language():
            sql.execute("""CREATE TABLE IF NOT EXISTS user_languages (
                user_id TEXT PRIMARY KEY, 
                language TEXT)""")

        def subs():
            sql.execute("""CREATE TABLE IF NOT EXISTS subs (
                user_id TEXT PRIMARY KEY,
                last_update TEXT,
                reg_date TEXT
            )""")

        def stages():
            sql.execute("""CREATE TABLE IF NOT EXISTS stages (
                user_id TEXT PRIMARY KEY,
                stage TEXT
            )""")

        def works():
            sql.execute("""CREATE TABLE IF NOT EXISTS works (
                work_id TEXT PRIMARY KEY,
                name TEXT,
                description_ru TEXT,
                description_he TEXT,
                description_en TEXT,
                day_work_time TEXT,
                day_price_per_hour TEXT,
                night_work_time TEXT,
                night_price_per_hour TEXT,
                food TEXT,
                city_ru TEXT,
                city_he TEXT,
                city_en TEXT,
                travel_expense_coverage TEXT,
                requirements_ru TEXT,
                requirements_he TEXT,
                requirements_en TEXT,
                status TEXT
            )""")

        def workers():
            sql.execute("""CREATE TABLE IF NOT EXISTS workers (
                user_id TEXT PRIMARY KEY,
                name TEXT,
                personal_id TEXT,
                age TEXT,
                sex TEXT,
                phone TEXT,
                phone2 TEXT,
                city TEXT,
                work_id TEXT,
                start_date TEXT,
                reg_date TEXT,
                status TEXT
            )""")

        def submissions():
            sql.execute("""CREATE TABLE IF NOT EXISTS submissions (
                user_id TEXT PRIMARY KEY,
                work_id TEXT,
                status TEXT,
                date_of_submission TEXT
            )""")

        def posts():
            sql.execute("""CREATE TABLE IF NOT EXISTS posts (
                post_id TEXT PRIMARY KEY,
                ad_id TEXT,
                group_id TEXT,
                post_time TEXT)""")

        for i in [user_language, subs, stages, works, workers, submissions, posts]:
            i()
            if DEBUG:
                print(f"[+] Table {i.__name__} created")

        db.commit()
        if DEBUG:
            print("[+] Committed")


prepare_db()


class UserLanguage:
    def __init__(self, user_id):
        self.user_id = user_id
        self.language = "en"

    def get(self):
        with Database() as (db, sql):
            sql.execute(f"SELECT * FROM user_languages WHERE user_id = '{str(self.user_id)}'")
            result = sql.fetchone()
            if result is None:
                return None
            else:
                return result[1]

    def set(self, language):
        with Database() as (db, sql):
            sql.execute(f"SELECT * FROM user_languages WHERE user_id = '{str(self.user_id)}'")
            result = sql.fetchone()
            if result is None:
                sql.execute(f"INSERT INTO user_languages VALUES ('{str(self.user_id)}', '{str(language)}')")
            else:
                sql.execute(f"UPDATE user_languages SET language = '{str(language)}' WHERE user_id = '{str(self.user_id)}'")
            db.commit()


class Sub:
    def __init__(self, user_id):
        self.user_id = user_id

    def update(self):
        with Database() as (db, sql):
            sql.execute(f"SELECT * FROM subs WHERE user_id = '{str(self.user_id)}'")
            result = sql.fetchone()
            if result is None:
                sql.execute(
                    f"INSERT INTO subs VALUES ('{str(self.user_id)}', '{str(datetime.datetime.now())}', '{str(datetime.datetime.now())}')")
            else:
                sql.execute(
                    f"UPDATE subs SET last_update = '{str(datetime.datetime.now())}' WHERE user_id = '{str(self.user_id)}'")
            db.commit()


class Stage:
    def __init__(self, user_id):
        self.user_id = user_id

    def get(self):
        with Database() as (db, sql):
            sql.execute(f"SELECT * FROM stages WHERE user_id = '{str(self.user_id)}'")
            result = sql.fetchone()
            if result is None:
                return "None"
            else:
                return result[1]

    def set(self, stage):
        with Database() as (db, sql):
            sql.execute(f"SELECT * FROM stages WHERE user_id = '{str(self.user_id)}'")
            result = sql.fetchone()
            if result is None:
                sql.execute(f"INSERT INTO stages VALUES ('{str(self.user_id)}', '{str(stage)}')")
            else:
                sql.execute(f"UPDATE stages SET stage = '{str(stage)}' WHERE user_id = '{str(self.user_id)}'")
            db.commit()


class Work:
    def __init__(self, work_id=None):
        self.work_id = work_id
        self.name = None
        self.description_ru = None
        self.description_he = None
        self.description_en = None
        self.day_work_time = None
        self.day_price_per_hour = None
        self.night_work_time = None
        self.night_price_per_hour = None
        self.food = None
        self.city_ru = None
        self.city_he = None
        self.city_en = None
        self.travel_expense_coverage = None
        self.requirements_ru = None
        self.requirements_he = None
        self.requirements_en = None
        self.status = None

    def get(self) -> "None | Work | list[Work]":
        with Database() as (db, sql):
            if self.work_id:
                sql.execute(f"SELECT * FROM works WHERE work_id = '{str(self.work_id)}'")
                result = sql.fetchone()
                if result is None:
                    return None
                else:
                    self.name = result[1]
                    self.description_ru = result[2]
                    self.description_he = result[3]
                    self.description_en = result[4]
                    self.day_work_time = result[5]
                    self.day_price_per_hour = result[6]
                    self.night_work_time = result[7]
                    self.night_price_per_hour = result[8]
                    self.food = result[9]
                    self.city_ru = result[10]
                    self.city_he = result[11]
                    self.city_en = result[12]
                    self.travel_expense_coverage = result[13]
                    self.requirements_ru = result[14]
                    self.requirements_he = result[15]
                    self.requirements_en = result[16]
                    return self

            else:
                sql.execute(f"SELECT * FROM works")
                result = sql.fetchall()
                if result is None:
                    return None
                else:
                    r = []
                    for i in result:
                        w = Work(i[0])
                        w.name = i[1]
                        w.description_ru = i[2]
                        w.description_he = i[3]
                        w.description_en = i[4]
                        w.day_work_time = i[5]
                        w.day_price_per_hour = i[6]
                        w.night_work_time = i[7]
                        w.night_price_per_hour = i[8]
                        w.food = i[9]
                        w.city_ru = i[10]
                        w.city_he = i[11]
                        w.city_en = i[12]
                        w.travel_expense_coverage = i[13]
                        w.requirements_ru = i[14]
                        w.requirements_he = i[15]
                        w.requirements_en = i[16]
                        w.status = i[17]
                        r.append(w)
                    return r

    def insert(self):
        with Database() as (db, sql):
            sql.execute(f"""INSERT INTO works VALUES (
            '{str(self.work_id)}',
            '{str(self.name)}',
            '{str(self.description_ru)}',
            '{str(self.description_he)}',
            '{str(self.description_en)}',
            '{str(self.day_work_time)}',
            '{str(self.day_price_per_hour)}',
            '{str(self.night_work_time)}',
            '{str(self.night_price_per_hour)}',
            '{str(self.food)}',
            '{str(self.city_ru)}',
            '{str(self.city_he)}',
            '{str(self.city_en)}',
            '{str(self.travel_expense_coverage)}',
            '{str(self.requirements_ru)}',
            '{str(self.requirements_he)}',
            '{str(self.requirements_en)}',
            '{str(self.status)}')""")
            db.commit()

    def update(self, column, value):
        with Database() as (db, sql):
            sql.execute(f"UPDATE works SET {str(column)} = '{str(value)}' WHERE work_id = '{str(self.work_id)}'")
            db.commit()


class Worker:
    """
    user_id TEXT PRIMARY KEY,
    name TEXT,
    personal_id TEXT,
    age TEXT,
    sex TEXT,
    phone TEXT,
    phone2 TEXT,
    city TEXT,
    work_id TEXT,
    start_date TEXT,
    reg_date TEXT,
    status TEXT
    """
    def __init__(self, user_id=None):
        self.user_id = user_id
        self.name = None
        self.personal_id = None
        self.age = None
        self.sex = None
        self.phone = None
        self.phone2 = None
        self.city = None
        self.work_id = None
        self.start_date = None
        self.reg_date = None
        self.status = None

    def get(self):
        with Database() as (db, sql):
            if self.user_id:
                sql.execute(f"SELECT * FROM workers WHERE user_id = '{str(self.user_id)}'")
                result = sql.fetchone()
                if result is None:
                    return None
                else:
                    self.name = result[1]
                    self.personal_id = result[2]
                    self.age = result[3]
                    self.sex = result[4]
                    self.phone = result[5]
                    self.phone2 = result[6]
                    self.city = result[7]
                    self.work_id = result[8]
                    self.start_date = result[9]
                    self.reg_date = result[10]
                    self.status = result[11]
                    return self

            else:
                sql.execute(f"SELECT * FROM workers")
                result = sql.fetchall()
                if result is None:
                    return None
                else:
                    r = []
                    for i in result:
                        w = Worker(i[0])
                        w.name = i[1]
                        w.personal_id = i[2]
                        w.age = i[3]
                        w.sex = i[4]
                        w.phone = i[5]
                        w.phone2 = i[6]
                        w.city = i[7]
                        w.work_id = i[8]
                        w.start_date = i[9]
                        w.reg_date = i[10]
                        w.status = i[11]
                        r.append(w)
                    return r

    def insert(self):
        with Database() as (db, sql):
            sql.execute(f"""INSERT INTO workers VALUES (
            '{str(self.user_id)}',
            '{str(self.name)}',
            '{str(self.personal_id)}',
            '{str(self.age)}',
            '{str(self.sex)}',
            '{str(self.phone)}',
            '{str(self.phone2)}',
            '{str(self.city)}',
            '{str(self.work_id)}',
            '{str(self.start_date)}',
            '{str(self.reg_date)}',
            '{str(self.status)}')""")
            db.commit()

    def update(self, column, value):
        with Database() as (db, sql):
            sql.execute(f"UPDATE workers SET {str(column)} = '{str(value)}' WHERE user_id = '{str(self.user_id)}'")
            db.commit()


class Submission:
    """
    user_id TEXT PRIMARY KEY,
    work_id TEXT,
    status TEXT,
    date_of_submission TEXT
    """
    def __init__(self, user_id=None):
        self.user_id = user_id
        self.work_id = None
        self.status = None
        self.date_of_submission = None

    def get(self):
        with Database() as (db, sql):
            if self.user_id:
                sql.execute(f"SELECT * FROM submissions WHERE user_id = '{str(self.user_id)}'")
                result = sql.fetchone()
                print(result)
                if result is None:
                    return None
                else:
                    self.work_id = result[1]
                    self.status = result[2]
                    self.date_of_submission = result[3]
                    return self

            else:
                sql.execute(f"SELECT * FROM submissions")
                result = sql.fetchall()
                if result is None:
                    return None
                else:
                    r = []
                    for i in result:
                        s = Submission(i[0])
                        s.work_id = i[1]
                        s.status = i[2]
                        s.date_of_submission = i[3]
                        r.append(s)
                    return r

    def insert(self):
        with Database() as (db, sql):
            sql.execute(f"""INSERT INTO submissions VALUES (
            '{str(self.user_id)}',
            '{str(self.work_id)}',
            '{str(self.status)}',
            '{str(self.date_of_submission)}')""")
            db.commit()

    def update(self, column, value):
        with Database() as (db, sql):
            sql.execute(f"UPDATE submissions SET {str(column)} = '{str(value)}' WHERE user_id = '{str(self.user_id)}'")
            db.commit()

    def delete(self):
        with Database() as (db, sql):
            sql.execute(f"DELETE FROM submissions WHERE user_id = '{str(self.user_id)}'")
            db.commit()


class Post:
    def __init__(self, group_id=None, ad_id=None):
        self.post_id = None
        self.ad_id = ad_id
        self.group_id = group_id
        self.post_time = None

    def get_all(self):
        with Database() as (db, sql):
            if self.group_id:
                command = f"SELECT * FROM posts WHERE group_id = '{str(self.group_id)}'"
            if self.ad_id and self.group_id:
                command += f" AND ad_id = '{str(self.ad_id)}'"
            else:
                command = f"SELECT * FROM posts"
            sql.execute(command)
            result = sql.fetchall()

            r = []
            for i in result:
                p = Post()
                p.post_id = i[0]
                p.ad_id = i[1]
                p.group_id = i[2]
                p.post_time = datetime.datetime.strftime(i[3], "%Y-%m-%d %H:%M:%S")
                r.append(p)
            r.sort(key=lambda x: x.post_time, reverse=True)
            return r

    def last_message_time(self):
        last_message = self.get_all()[0]
        return last_message.post_time

    def add(self):
        with Database() as (db, sql):
            sql.execute(f"""INSERT INTO posts VALUES (
            '{str(self.post_id)}',
            '{str(self.ad_id)}',
            '{str(self.group_id)}',
            '{str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))}')""")
            db.commit()


def get_content(user_id, text_id):
    default_lng = "he"
    lng = UserLanguage(user_id).get()
    if lng is None:
        lng = default_lng
    return eval(f"texts.Content.{text_id}")[lng]


def get_button(user_id, text_id):
    default_lng = "he"
    lng = UserLanguage(user_id).get()
    if lng is None:
        lng = default_lng
    return eval(f"texts.Button.{text_id}")[lng]


def back_btn(user_id, callback_data):
    return btn(get_button(user_id, "back"), callback_data=callback_data)


