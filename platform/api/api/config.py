"""
CTF API Configuration File

Note this is just a python script. It does config things.
"""

import api
import datetime

import api.app

""" FLASK """

api.app.session_cookie_domain = "innoctf.com"
api.app.session_cookie_path = "/"
api.app.session_cookie_name = "flask"

# KEEP THIS SECRET
api.app.secret_key = "cc89b310b81a4ddd93f59242c1556f13"

""" SECURITY """

api.common.allowed_protocols = ["https", "http"]
api.common.allowed_ports = [8080]

""" MONGO """

api.common.mongo_db_name = "pico"
api.common.mongo_addr = "mongodb"
api.common.mongo_port = 27017

""" TESTING """

testing_mongo_db_name = "ctf_test"
testing_mongo_addr = "mongodb"
testing_mongo_port = 27017

""" CTF SETTINGS """

enable_teachers = False
enable_feedback = True

competition_name = "InnoCTF"
#competition_urls = ["ctf.university.innopolis.ru:8080"]
competition_urls = ["innoctf.com"]

# Max users on any given team
api.team.max_team_users = 5

# Teams to display on scoreboard graph
api.stats.top_teams = 5 

# start and end times!
class EST(datetime.tzinfo):
    def __init__(self, utc_offset):
        self.utc_offset = utc_offset

    def utcoffset(self, dt):
      return datetime.timedelta(hours=-self.utc_offset)

    def dst(self, dt):
        return datetime.timedelta(0)

start_time = datetime.datetime(2015, 11, 20, 10, 30, 0)
end_time = datetime.datetime(2015, 11, 20, 15, 30, 0)

# Root directory of all problem graders
api.problem.grader_base_path = "./graders"

""" ACHIEVEMENTS """

enable_achievements = True

api.achievement.processor_base_path = "./achievements"

""" SHELL SERVER """

enable_shell = False

shell_host = "127.0.0.1"
shell_username = "vagrant"
shell_password = "vagrant"
shell_port = 22

shell_user_prefixes  = list("abcdefghijklmnopqrstuvwxyz")
shell_password_length = 4
shell_free_acounts = 10
shell_max_accounts = 9999

shell_user_creation = "sudo useradd -m {username} -p {password}"

""" EMAIL (SMTP) """

api.utilities.enable_email = True
api.utilities.smtp_url = "smtp.yandex.ru:465"
api.utilities.email_username = "admin@innoctf.com"
api.utilities.email_password = "9SDde5V05GcQdOtBGipi"
api.utilities.from_addr = "admin@innoctf.com"
api.utilities.from_name = "InnoCTF support"

""" CAPTCHA """
enable_captcha = False # don't enable. it is buggy :(
captcha_url = "https://www.google.com/recaptcha/api/siteverify"
reCAPTCHA_private_key = "6LeqewkUAAAAABuaenrh78xHblFqVXLvmAe3jYcR"


""" AUTOGENERATED PROBLEMS """

api.autogen.seed = "be30f7b00c5db6ed64e798d79ed24b4c"

""" LOGGING """

# Will be emailed any severe internal exceptions!
# Requires email block to be setup.
api.logger.admin_emails = ["admin@innoctf.com"]
api.logger.critical_error_timeout = 600
