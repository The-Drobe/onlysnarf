import os
from pathlib import Path

##
# Defaults 
##

AMOUNT_NONE = 0


CATEGORIES = [ "images", "galleries", "videos", "performers" ]
CATEGORY_NONE = CATEGORIES[0]

DEFAULT_MESSAGE = ":)"
DEFAULT_REFRESHER = "hi!"
DEFAULT_GREETING = "hi! thanks for subscribing :3 do you have any preferences?"

DISCOUNT_MAX_AMOUNT = 55
DISCOUNT_MIN_AMOUNT = 10
DISCOUNT_MAX_MONTHS = 7
DISCOUNT_MIN_MONTHS = 1

DATE_NONE = None

DURATION_ALLOWED = [1,3,7,30,99] # in days
DURATION_NONE = 0

EXPIRATION_MIN = 1
EXPIRATION_MAX = 30
EXPIRATION_NONE = 0

IMAGE_LIMIT = 15

LIMIT_ALLOWED = [0,1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100] # in %

MESSAGE_CHOICES = ["all", "recent", "favorite", "renew on"]

PROMOTION_EXPIRATION_ALLOWED = [int(i) for i in range(30)] # in %
PROMOTION_EXPIRATION_ALLOWED.insert(0,0)
# number
PROMOTION_OFFER_LIMIT = [0,1,2,3,4,5,6,7,8,9,10]
# various datetime
PROMOTION_DURATION_ALLOWED = ["1 day","3 days","7 days","14 days","1 month","3 months","6 months","12 months"]


PRICE_MINIMUM = 3

# sftp
# selenium browser
REMOTE_BROWSER = "127.0.0.1"
BROWSER_PORT = 4444

REMOTE_HOST = "127.0.0.1"
REMOTE_PORT = 22

SOURCES = [ "local","remote" ]

UPLOAD_MAX_DURATION = 6*6 # increments of 10 minutes; 6 = 1 hr

USER_LIMIT = 10

#########
# Paths #
#########

USER = os.getenv('USER')
if str(os.getenv('SUDO_USER')) != "root" and str(os.getenv('SUDO_USER')) != "None":
    USER = os.getenv('SUDO_USER')
USER_HOME = "/home/{}".format(USER)

ROOT_PATH = "{}/OnlySnarf".format(USER_HOME)
DOWNLOAD_PATH = os.path.join(ROOT_PATH, "downloads")
UPLOAD_PATH = os.path.join(ROOT_PATH, "uploads")
LOG_PATH = os.path.join(ROOT_PATH, "snarf.log")
REMOTE_PATH = ROOT_PATH
CONFIGS_PATH = "{}/.onlysnarf".format(USER_HOME)
USERS_PATH = os.path.join(CONFIGS_PATH, "users.json")
PROFILE_PATH = os.path.join(CONFIGS_PATH, "profile.json")
CONFIG_PATH = os.path.join(CONFIGS_PATH, "config.conf")
PROFILES_PATH = os.path.join(CONFIGS_PATH, "users")

if os.environ.get('ENV') == "test":
    print("Paths:")
    print("root: "+ROOT_PATH)
    print("configs: "+CONFIGS_PATH)
    print("config: "+CONFIG_PATH)
    print("download: "+DOWNLOAD_PATH)
    print("log: "+LOG_PATH)
    print("profiles: "+PROFILES_PATH)
    print("profile: "+PROFILE_PATH)
    print("remote: "+REMOTE_PATH)
    print("upload: "+UPLOAD_PATH)
    print("users: "+USERS_PATH)

Path(ROOT_PATH).mkdir(parents=True, exist_ok=True)
Path(DOWNLOAD_PATH).mkdir(parents=True, exist_ok=True)
Path(UPLOAD_PATH).mkdir(parents=True, exist_ok=True)
Path(CONFIGS_PATH).mkdir(parents=True, exist_ok=True)
