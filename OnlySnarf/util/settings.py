import pkg_resources
import time
import PyInquirer
import os, json, sys
from pathlib import Path
##
from .colorize import colorize
from .config import config
from . import defaults as DEFAULT
from .logger import logging
log = logging.getLogger('onlysnarf')

class Settings:
    
    LAST_UPDATED_KEY = None
    CATEGORY = None
    CONFIRM = True
    FILES = None
    PERFORMER_CATEGORY = None
    PROMPT = True

    def __init__():
        pass

    #####################
    ##### Functions #####
    #####################

    def debug_delay_check():
        if Settings.is_debug() == "True" and Settings.is_debug_delay() == "True":
            time.sleep(int(10))

    ##
    # Print
    ##

    def print(text):
        if int(config["verbose"]) >= 1:
            log.info(text)

    def print_same_line(text):
        sys.stdout.write('\r')
        sys.stdout.flush()
        sys.stdout.write(text)
        sys.stdout.flush()

    def maybe_print(text):
        if int(config["verbose"]) >= 2:
            log.debug(text)

    def dev_print(text):
        if int(config["verbose"]) >= 3:
            log.debug(text)

    def err_print(error):
        log.error(error)

    def warn_print(error):
        log.warning(error)

    ##
    # Getters
    ##

    def get_action():
        return config["action"]

    def get_actions():
        return DEFAULT.ACTIONS

    def get_amount():
        return config["amount"]

    def get_base_directory():
        USER = os.getenv('USER')
        if str(os.getenv('SUDO_USER')) != "root" and str(os.getenv('SUDO_USER')) != "None":
            USER = os.getenv('SUDO_USER')
        baseDir = "/home/{}/.onlysnarf".format(USER)
        # if os.environ.get('ENV') == "test":
          # baseDir = os.getcwd()
          # baseDir = os.path.dirname(__file__)
        return baseDir

    def get_browser_type():
        return config["browser"]

    def get_months():
        return config["months"]

    def get_category():
        cat = config["category"]
        if str(cat) == "image": cat = "images"
        if str(cat) == "gallery": cat = "galleries"
        if str(cat) == "video": cat = "videos"
        if str(cat) == "performer": cat = "performers"
        return cat or None

    def get_categories():
        cats = []
        cats.extend(list(DEFAULT.CATEGORIES))
        cats.extend(list(config["categories"]))
        return cats

    def get_cookies_path():
        # return os.path.join(Settings.get_base_directory(), Settings.get_username(), "cookies.pkl")
        return os.path.join(Settings.get_base_directory(), "cookies.pkl")

    def get_price():
        return config["price"] or ""

    def get_price_minimum():
        return DEFAULT.PRICE_MINIMUM or 0

    def get_date():
        return config["date"] or None

    def get_default_greeting():
        return DEFAULT.GREETING or ""

    def get_default_refresher():
        return DEFAULT.REFRESHER or ""
        
    def get_discount_max_amount():
        return DEFAULT.DISCOUNT_MAX_AMOUNT or 0
        
    def get_discount_min_amount():
        return DEFAULT.DISCOUNT_MIN_AMOUNT or 0
        
    def get_discount_max_months():
        return DEFAULT.DISCOUNT_MAX_MONTHS or 0
        
    def get_discount_min_months():
        return DEFAULT.DISCOUNT_MIN_MONTHS or 0

    def get_download_max():
        return config["image_limit"] or DEFAULT.IMAGE_LIMIT
        
    def get_drive_ignore():
        return config["notkeyword"] or None
        
    def get_drive_keyword():
        return config["bykeyword"] or None
        
    def get_duration():
        return config["duration"] or None

    def get_promo_duration():
        return config["duration_promo"] or None
        
    def get_duration_allowed():
        return DEFAULT.DURATION_ALLOWED or []
        
    def get_duration_promo_allowed():
        return DEFAULT.PROMOTION_DURATION_ALLOWED or []

    def get_expiration():
        return config["expiration"] or config["promotion_expiration"] or None
        
    def get_expiration_allowed():
        return DEFAULT.EXPIRATION_ALLOWED or []

    def get_input():
        return config["input"] or []

    def get_input_as_files():
        if Settings.FILES: return Settings.FILES
        from ..classes.file import File
        files = []
        if isinstance(config["input"], list):
            for file_path in config["input"]:
                file = File()
                setattr(file, "path", file_path)
                files.append(file)
        else:
            file = File()
            setattr(file, "path", config["input"])
            files.append(file)
        Settings.FILES = files
        return files

    def get_keywords():
        keywords = config["keywords"] or []
        keywords = [n.strip() for n in keywords]
        return keywords

    def get_logs_path(process):
        if process == "firefox":
            path_ = os.path.join(Settings.get_base_directory(), "log")
            Path(path_).mkdir(parents=True, exist_ok=True)
            return os.path.join(path_, "geckodriver.log")
        elif process == "google":
            path_ = os.path.join(Settings.get_base_directory(), "log")
            Path(path_).mkdir(parents=True, exist_ok=True)
            return os.path.join(path_, "chromedriver.log")
        return ""

    def get_message_choices():
        return DEFAULT.MESSAGE_CHOICES

    def get_root_path():
        return config["root_path"] or DEFAULT.ROOT_PATH

    def get_sort_method():
        return config["sort"] or "random"

    def get_performers():
        performers = config["performers"] or []
        performers = [n.strip() for n in performers]
        return performers

    def get_profile_path():
        return config["profile_path"] or DEFAULT.PROFILE_PATH

    def get_recent_user_count():
        return config["recent_users_count"] or 0
    
    def get_promotion_limit():
        return config["promotion_limit"] or None

    def get_promotion_method():
        return config["promotion_method"] or None

    def get_password():
        try:
            return config["password"] or Settings.get_user_config(Settings.get_username())["onlyfans_password"]
        except Exception as e:
            Settings.err_print(e)
        return ""

    def get_password_google():
        try:
            return config["google_password"] or Settings.get_user_config(Settings.get_username())["google_password"]
        except Exception as e:
            Settings.err_print(e)
        return ""

    def get_password_twitter():
        try:
            return config["twitter_password"] or Settings.get_user_config(Settings.get_username())["twitter_password"]
        except Exception as e:
            Settings.err_print(e)
        return ""

    def get_download_path():
        return config["download_path"] or ""

    def get_users_path():
        return config["path_users"] or DEFAULT.USERS_PATH

    def get_config_path():
        return config["config_path"] or ""    

    def get_local_path():
        localPath = os.path.join(Settings.get_root_path(), Settings.get_username())
        from pathlib import Path
        Path(localPath).mkdir(parents=True, exist_ok=True)
        for cat in Settings.get_categories():
            Path(os.path.join(localPath, cat)).mkdir(parents=True, exist_ok=True)
        return localPath

    def get_destination():
        return config["destination"] or ""

    def get_source():
        return config["source"] or ""

    def get_source_options():
        return DEFAULT.SOURCES

    def get_reconnect_id():
        return config["session_id"] or ""

    def get_reconnect_url():
        return config["session_url"] or ""

    def get_remote_host():
        return config["remote_host"] or DEFAULT.REMOTE_HOST

    def get_remote_port():
        return config["remote_port"] or DEFAULT.REMOTE_PORT

    def get_remote_path():
        return config["remote_path"] or DEFAULT.REMOTE_PATH

    def get_remote_username():
        return config["remote_username"] or ""

    def get_remote_password():
        return config["remote_password"] or ""

    def get_remote_browser_host():
        return config["remote_browser_host"] or DEFAULT.REMOTE_BROWSER

    def get_remote_browser_port():
        return config["remote_browser_port"] or DEFAULT.BROWSER_PORT

    def get_profile_method():
        return config["profile_method"] or None

    def get_schedule():
        if str(config["schedule"]) != "None": return config["schedule"]
        if Settings.get_date():
            if Settings.get_time():
                config["schedule"] = "{} {}".format(Settings.get_date(), Settings.get_time())
            else:
                config["schedule"] = "{}".format(Settings.get_date())
        return config["schedule"]

    def get_tags():
        tags = config["tags"] or []
        tags = [n.strip() for n in tags]
        return tags

    def get_text():
        return config["text"] or None

    def get_time():
        return config["time"] or None

    def get_title():
        return config["title"] or None
        
    def get_skipped_users():
        return config["skipped_users"] or []
        
    def get_questions():
        return config["questions"] or []
        
    def get_upload_max():
        return config["image_limit"] or DEFAULT.IMAGE_LIMIT
        
    # def get_upload_max_messages():
        # return config["upload_max_messages"] or UPLOAD_MAX_MESSAGES

    def get_login_method():
        return config["login"] or "onlyfans"
        
    def get_upload_max_duration():
        return config["upload_max_duration"] or DEFAULT.UPLOAD_MAX_DURATION # 6 hours

    # comma separated string of usernames
    def get_users():
        users = config["users"] or []
        users = [n.strip() for n in users]
        from ..classes.user import User
        users_ = []
        for user in users:
            # user = User({})
            user = User({"username":config["user"]})
            # setattr(user, "username", config["user"])
            from ..lib.driver import Driver
            setattr(user, "driver", Driver.get_driver())
            users_.append(user)
        return users_

    def get_user():
        if not config["user"]: return None
        from ..classes.user import User
        return User({"username":config["user"]})

    def get_email():
        return config["email"] or ""

    def get_user_configs():
        # load configs from .onlysnarf or baseDir
        pass

    def get_user_config(username="default"):
        import configparser
        config_file = configparser.ConfigParser()
        # strip email
        if "@" in username: username = username[0 : username.index("@")]
        config_file.read(os.path.join(Settings.get_base_directory(), "users", username+".conf"))
        userConfig = {}
        for section in config_file.sections():
            # print(section)
            for key in config_file[section]:
                # print(section, key, config_file[section][key].strip("\""))
                userConfig[section.lower()+"_"+key.lower()] = config_file[section][key].strip("\"")
        return userConfig

    def get_username():
        return config["username"] or ""

    def get_username_onlyfans():
        try:
            return Settings.get_user_config(Settings.get_username())["onlyfans_username"]
        except Exception as e:
            Settings.err_print(e)
        return ""

    def get_username_google():
        try:
            return config["google_username"] or Settings.get_user_config(Settings.get_username())["google_username"]
        except Exception as e:
            Settings.err_print(e)
        return ""            

    def get_username_twitter():
        try:
            return config["twitter_username"] or Settings.get_user_config(Settings.get_username())["twitter_username"]
        except Exception as e:
            Settings.err_print(e)
        return ""

    ## TODO
    # add arg -profile
    # add method for reading config profiles from conf/users

    def get_profile():
        pass

    def select_profile():
        pass



    # def get_users_favorite():
    #     return config["users_favorite"] or []
        
    def get_verbosity():
        return config["verbose"] or 0

    def get_version():
        return pkg_resources.get_distribution("onlysnarf").version

    def get_user_num():
        return config["users_read"] or DEFAULT.USER_LIMIT

    # Bools

    def is_confirm():
        return Settings.CONFIRM or False

    def is_cookies():
        return config["cookies"] or False

    def is_delete_empty():
        return config["delete_empty"] or False

    def is_prompt():
        return Settings.PROMPT or False

    def is_debug(process=None):
        if process == "firefox": return config["debug_firefox"]
        elif process == "google": return config["debug_google"]
        elif process == "selenium": return config["debug_selenium"]
        return config["debug"] or False

    def is_debug_delay():
        return config["debug_delay"] or False

    def is_force_backup():
        return config["force_backup"] or False

    def is_force_upload():
        return config["force_upload"] or False

    def is_keep():
        return config["keep"] or False

    def is_prefer_local():
        return config["prefer_local"] or False

    def is_save_users():
        return config["save_users"] or False
        
    def is_reduce():
        return config["enable_reduce"] or False
    
    def is_show_window():
        return config["show"] or False

    def is_split():
        return config["enable_split"] or False
        
    def is_trim():
        return config["enable_trim"] or False
        
    def is_tweeting():
        return config["tweeting"] or False
        
    def is_backup():
        return config["backup"] or False
        
    def is_skip_download():
        return config["skip_download"] or False
        
    def is_skip_upload():
        return config["skip_upload"] or False

    ##
    # Menu
    ##

    def confirm(text):
        try:
            if text == None: return False
            if list(text) == []: return False
            if str(text) == "": return False
            if not Settings.CONFIRM: return True
        except: pass
        questions = [
            {
                'type': 'confirm',
                'message': 'Is this correct? -> {}'.format(text),
                'name': 'confirm',
                'default': True,
            }
        ]
        return PyInquirer.prompt(questions)["confirm"]

    def header():
        if Settings.LAST_UPDATED_KEY is not None:
            print("Updated: {} = {}".format(Settings.LAST_UPDATED_KEY, config[str(Settings.LAST_UPDATED_KEY).replace(" ","_").lower()]))
            print('\r')
        Settings.LAST_UPDATED_KEY = None

    def menu():
        skipList = ["action", "amount", "category", "categories", "cron", "input", "messages", "posts", "date", "duration", "expiration", "keywords", "limit", "months", "bykeyword", "notkeyword", "price", "config_path", "questions", "schedule", "skipped_users", "tags", "text", "time", "title", "user", "users", "username", "password", "users_favorite"]
        print('Settings')
        keys = [key.replace("_"," ").title() for key in config.keys() if key.lower() not in skipList and "categories" not in str(key).lower() and "messages" not in str(key).lower()]
        keys.insert(0, "Back")
        question = {
            'type': 'list',
            'name': 'choice',
            'message': 'Set:',
            'choices': keys,
            'filter': lambda val: val.lower()
        }
        answer = PyInquirer.prompt(question)["choice"]
        if str(answer).lower() == "back": return
        Settings.set_setting(answer.replace(" ", "_"))

    def prompt(text):
        if list(text) == []: return False
        if str(text) == "": return False
        if not Settings.PROMPT: return False
        question = {
            'type': 'confirm',
            'message': '{}?'.format(str(text).capitalize()),
            'name': 'confirm',
            'default': True,
        }
        return PyInquirer.prompt(question)["confirm"]

    def prompt_email():
        if not Settings.PROMPT: return False
        question = {
            'type': 'input',
            'message': 'Email:',
            'name': 'email'
        }
        email = PyInquirer.prompt(question)["email"]
        Settings.set_email(email)
        return email

    def prompt_username():
        if not Settings.PROMPT: return False
        question = {
            'type': 'input',
            'message': 'Username:',
            'name': 'username'
        }
        username = PyInquirer.prompt(question)["username"]
        Settings.set_username(username)
        return username

    def prompt_password():
        if not Settings.PROMPT: return False
        question = {
            'type': 'password',
            'message': 'Password:',
            'name': 'password'
        }
        pw = PyInquirer.prompt(question)["password"]
        Settings.set_password(pw)
        return pw

    def prompt_username_google():
        if not Settings.PROMPT: return False
        question = {
            'type': 'input',
            'message': 'Google username:',
            'name': 'username'
        }
        username = PyInquirer.prompt(question)["username"]
        Settings.set_username_google(username)
        return username

    def prompt_password_google():
        if not Settings.PROMPT: return False
        question = {
            'type': 'password',
            'message': 'Google password:',
            'name': 'password'
        }
        pw = PyInquirer.prompt(question)["password"]
        Settings.set_password_google(pw)
        return pw

    def prompt_username_twitter():
        if not Settings.PROMPT: return False
        question = {
            'type': 'input',
            'message': 'Twitter username:',
            'name': 'username'
        }
        username = PyInquirer.prompt(question)["username"]
        Settings.set_username_twitter(username)
        return username

    def prompt_password_twitter():
        if not Settings.PROMPT: return False
        question = {
            'type': 'password',
            'message': 'Twitter password:',
            'name': 'password'
        }
        pw = PyInquirer.prompt(question)["password"]
        Settings.set_password_twitter(pw)
        return pw

    def read_session_data():
        Settings.maybe_print("reading local session")
        path_ = os.path.join(Settings.get_base_directory(), "session.json")
        Settings.dev_print("local session path: "+str(path_))
        id_ = None
        url = None
        try:
            with open(str(path_)) as json_file:  
                data = json.load(json_file)
                id_ = data['id']
                url = data['url']
            Settings.maybe_print("loaded local users")
        except Exception as e:
            Settings.dev_print(e)
        return (id_, url)

    def write_session_data(id_, url):
        Settings.maybe_print("writing local session")
        Settings.dev_print("saving session id: {}".format(id_))        
        Settings.dev_print("saving session url: {}".format(url))
        path_ = os.path.join(Settings.get_base_directory(), "session.json")
        Settings.dev_print("local session path: "+str(path_))
        data = {}
        data['id'] = id_
        data['url'] = url
        try:
            with open(str(path_), 'w') as outfile:  
                json.dump(data, outfile, indent=4, sort_keys=True)
        except FileNotFoundError:
            Settings.err_print("Missing Session File")
        except OSError:
            Settings.err_print("Missing Session Path")

    def select_category(categories=None):
        # if Settings.CATEGORY: return Settings.CATEGORY
        if not categories: categories = Settings.get_categories()
        print("Select a Category")
        categories.insert(0, "Back")
        question = {
            'type': 'list',
            'message': 'Category:',
            'name': 'category',
            'choices': categories,
            'filter': lambda cat: cat.lower()
        }
        cat = PyInquirer.prompt(question)["category"]
        if str(cat) == "back": return None
        if not Settings.confirm(cat): return Settings.select_category()
        # Settings.CATEGORY = cat
        config["category"] = cat
        return cat

    ##
    # Setters
    ##

    def set_bycategory(cat):
        config["bycategory"] = cat

    def set_category(cat):
        config["category"] = cat

    def set_confirm(value):
        Settings.CONFIRM = bool(value)

    def set_email(email):
        config["email"] = str(email)

    def set_username(username):
        config["username"] = str(username)

    def set_username_google(username):
        config["username_google"] = str(username)

    def set_username_twitter(username):
        config["username_twitter"] = str(username)

    def set_password(password):
        config["password"] = str(password)

    def set_password_google(password):
        config["password_google"] = str(password)

    def set_password_twitter(password):
        config["password_twitter"] = str(password)

    def set_prefer_local(buul):
        config["prefer_local"] = bool(buul)
    
    def set_prefer_local_following(buul):
        config["prefer_local_following"] = bool(buul)

    def set_prompt(value):
        Settings.PROMPT = bool(value)

    def set_setting(key):
        try:
            value = config[key]
            key = key.replace("_"," ").title()
            print("Current: {}".format(value))
            if str(value) == "True" or str(value) == "False":
                question = {
                    'type': 'confirm',
                    'name': 'setting',
                    'message': "Toggle value?"
                }
                answer = PyInquirer.prompt(question)["setting"]
                if not answer: return Settings.menu()
                if bool(value): config[key.lower()] = False
                else: config[key.lower()] = True
            else:
                question = {
                    'type': 'input',
                    'name': 'setting',
                    'message': "New value:",
                    # 'default': int(value)
                }
                answer = PyInquirer.prompt(question)["setting"]
                if not Settings.confirm(answer): return Settings.menu()
                config[key.lower().replace(" ","_")] = answer
            Settings.LAST_UPDATED_KEY = key.lower()
        except Exception as e:
            Settings.dev_print(e)

###########################################################################



#     def update_value(self, variable, newValue):
#         variable = str(variable).upper().replace(" ","_")
#         try:
#             # print("Updating: {} = {}".format(variable, newValue))
#             setattr(self, variable, newValue)
#             # print("Updated: {} = {}".format(variable, getattr(self, variable)))
#         except Exception as e:
#             maybePrint(e)

# # move this behavior to user
#     def update_profile_value(self, variable, newValue):
#         variable = str(variable).upper().replace(" ","_")
#         try:
#             # print("Updating: {} = {}".format(variable, newValue))
#             Settings.PROFILE.setattr(self, variable, newValue)
#             # print("Updated: {} = {}".format(variable, getattr(self, variable)))
#         except Exception as e:
#             maybePrint(e)














































#######################################################################################

def delayForThirty():
    Settings.maybe_print("30...")
    time.sleep(10)
    Settings.maybe_print("20...")
    time.sleep(10)
    Settings.maybe_print("10...")
    time.sleep(7)
    Settings.maybe_print("3...")
    time.sleep(1)
    Settings.maybe_print("2...")
    time.sleep(1)
    Settings.maybe_print("1...")
    time.sleep(1)