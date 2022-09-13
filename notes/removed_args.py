###################################################################
##                          DEPRECATED                           ##
###################################################################
# these have all been moved from optionalargs to config file only #
###################################################################

##
# removed ?/?/2021
##

##
# configurable w/ profile.conf
# OnlySnarf Drive folder list, appends to defaults
parser.add_argument('-categories', dest='categories',
  action='append', help='the categories to list in menu (appends to \'{}\''.format("\'".join(CATEGORIES_DEFAULT)), 
  default=[])
##
# -create-missing 
# creates missing OnlySnarf folders
parser.add_argument('-create-missing', action='store_true', dest='create_missing',
  help='creates missing OnlySnarf folders at target source')

##
# -cron
# determines whether script running is a cronjob
parser.add_argument('-cron', action='store_true', help='toggle cron behavior', dest='cron')
##
# -cron-user
# the user to run OnlySnarf as
parser.add_argument('-cron-user', type=str, dest='cron_user',
  help='the user to run OnlySnarf as', default='root')

##
# -delete-empty
# delete empty content folders
parser.add_argument('-delete-empty', action='store_true', dest='delete_empty',
  help='delete empty content folders')

##
# download path
parser.add_argument('-download-path', type=str, dest='download_path',
  help='the path to download files to locally', default=DOWNLOAD_PATH)

# Combined / Deleted into new args

##
# -delete-google
# delete uploaded content instaed of backing it up
parser.add_argument('-delete-google', action='store_true', dest='delete_google',
  help='delete file instead of backing up')


##
# removed 9/9/2022
##



##
# -duration-promo
# promotion duration
parser.add_argument('-duration-promo', type=valid_promo_duration, dest='duration_promo',
  help='the duration in days (99 for \'No Limit\') for a promotion', choices=DEFAULT.PROMOTION_DURATION_ALLOWED, default=None)

##
# -email
# the OnlyFans email to use for login
parser.add_argument('-email', type=str, default="", dest='email',
  help='the email for an OnlyFans profile')

##
# -keywords
# keywords to # in post
parser.add_argument('-keywords', dest='keywords', action='append', default=[], 
  help="the keywords (#[keyword])")

##
# -bykeyword
# the keyword to search for in folder selection
parser.add_argument('-bykeyword', dest='bykeyword', default=None, 
  help="search for folder by keyword")
##
# -notkeyword
# the keyword to skip in folder selection
parser.add_argument('-notkeyword', dest='notkeyword', default=None,
  help="search for folder not by keyword")


##
# -prefer-local
# prefers local user cache over refreshing first call
parser.add_argument('-prefer-local', default=True, action='store_false', dest='prefer_local',
  help='prefer recently cached data')

##
# -repair
# enables file repair (buggy)
parser.add_argument('-repair', action='store_true', dest='repair',
  help='enable repairing videos as appropriate (buggy)')

##
# -recent-users-count
# the maximum number of recent users
parser.add_argument('-recent-users-count', default=3, dest='recent_users_count',
  type=int, help='the number of users to consider recent')

##
# -reduce
# enables file reduction
parser.add_argument('-reduce', action='store_true', dest='reduce',
  help='enable reducing files over 50 MB')



##
# -title
# the title of a file to search for
parser.add_argument('-title', default=None, dest='title',
  help='the title of the file to search for')



##
# -session-id
parser.add_argument('-session-id', default=None, dest='session_id',
  help='the session id to use')

# -session-url
parser.add_argument('-session-url', default=None, dest='session_url',
  help='the session url to use')

##
# -thumbnail
# attempt to fix thumbnail
parser.add_argument('-thumbnail', action='store_true', dest='thumbnail',
  help='fix thumbnails when necessary')

##
# -users-read
# the number of users read when checking messages
parser.add_argument('-users-read', type=int, dest='users_read',
  help='the number of users to read when checking messages', default=10)

## 
# -profile-method
parser.add_argument('-profile-method', dest="profile_method", default="syncfrom", choices=["syncto","syncfrom"],
  help='the profile method to use')

##
# -promotion
# the promotion method to use
parser.add_argument('-promotion-method', dest='promotion_method', default="campaign", choices=["campaign","trial","grandfather","user"],
  help='the promotion method to use')

##
# -promotion-user
parser.add_argument('-promotion-user', dest="promotion_user", action='store_true', 
  help="uses user method when combined with action=promotion")

##
# -root-path
# the root path for a local directory of OnlyFans config files
parser.add_argument('-root-path', dest='root_path',
  help='the local path to OnlySnarf processes')