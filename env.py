from decouple import config

# Get envs
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
SESSION = config("SESSION")
FROM_ = config("FROM_CHANNEL")
TO_ = config("TO_CHANNEL")
SEPARATE_CHANNELS = config(
    "SEPARATE_CHANNELS") == "1" or "True" or "true" or "TRUE" or "Yes" or "yes" or "YES"
BLACKLIST_WORDS_ = config("BLACKLIST_WORDS")
CHANGE_FOR_ = config("CHANGE_FOR")
THROW_IF_MESSAGE_CONSIST_WORDS_ = config("THROW_IF_MESSAGE_CONSIST_WORDS")
THROW_IF_MESSAGE_CONSIST_URL_ = config(
    "THROW_IF_MESSAGE_CONSIST_URL") == "1" or "True" or "true" or "TRUE" or "Yes" or "yes" or "YES"
DELETE_URL_FROM_MESSAGE_ = config(
    "DELETE_URL_FROM_MESSAGE") == "1" or "True" or "true" or "TRUE" or "Yes" or "yes" or "YES"

FROM = [int(i) for i in FROM_.split(";")]
TO = [int(i) for i in TO_.split(";")]

if len(FROM) == len(TO) and SEPARATE_CHANNELS:
    SEPARATE_CHANNELS = True
else:
    SEPARATE_CHANNELS = False

if len(BLACKLIST_WORDS_) == 0:
    BLACKLIST_WORDS = []
else:
    BLACKLIST_WORDS = [str(i) for i in BLACKLIST_WORDS_.split(";")]

if len(CHANGE_FOR_) == 0:
    CHANGE_FOR = []
else:
    CHANGE_FOR = [str(i) for i in CHANGE_FOR_.split(";")]

if len(THROW_IF_MESSAGE_CONSIST_WORDS_) == 0:
    THROW_IF_MESSAGE_CONSIST_WORDS = []
else:
    THROW_IF_MESSAGE_CONSIST_WORDS = [
        str(i) for i in THROW_IF_MESSAGE_CONSIST_WORDS_.split(";")]

if THROW_IF_MESSAGE_CONSIST_URL_ and DELETE_URL_FROM_MESSAGE_ == False:
    THROW_IF_MESSAGE_CONSIST_URL = True
    DELETE_URL_FROM_MESSAGE = False
elif THROW_IF_MESSAGE_CONSIST_URL_ == False and DELETE_URL_FROM_MESSAGE_:
    THROW_IF_MESSAGE_CONSIST_URL = False
    DELETE_URL_FROM_MESSAGE = True
else:
    THROW_IF_MESSAGE_CONSIST_URL = False
    DELETE_URL_FROM_MESSAGE = False
