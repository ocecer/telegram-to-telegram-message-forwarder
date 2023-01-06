from decouple import config

# Get envs
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
SESSION = config("SESSION")
FROM_ = config("FROM_CHANNEL")
TO_ = config("TO_CHANNEL")
SEPARATE_CHANNELS_ = config("SEPARATE_CHANNELS")
FORWARD_FROM_YOUR_OWN_CHANNELS_ = config("FORWARD_FROM_YOUR_OWN_CHANNELS")
BLACKLIST_WORDS_ = config("BLACKLIST_WORDS")
CHANGE_FOR_ = config("CHANGE_FOR")
THROW_IF_MESSAGE_CONSIST_WORDS_ = config("THROW_IF_MESSAGE_CONSIST_WORDS")
FORWARD_IF_MESSAGE_CONSIST_WORDS_ = config("FORWARD_IF_MESSAGE_CONSIST_WORDS")
THROW_IF_MESSAGE_CONSIST_URL_ = config("THROW_IF_MESSAGE_CONSIST_URL")
DELETE_URL_FROM_MESSAGE_ = config("DELETE_URL_FROM_MESSAGE")

FROM_ = FROM_.strip()
if FROM_.endswith(";"):
    FROM_ = FROM_.rstrip(FROM_[-1])

FROM = [int(i) for i in FROM_.split(";")]

TO_ = TO_.strip()
if TO_.endswith(";"):
    TO_ = TO_.rstrip(TO_[-1])

TO = [int(i) for i in TO_.split(";")]

trueCondition = ["1", "True", "true", "TRUE", "Yes", "yes", "YES"]

SEPARATE_CHANNELS = False
for condition in trueCondition:
    if SEPARATE_CHANNELS_ == condition:
        SEPARATE_CHANNELS = True
        break

THROW_IF_MESSAGE_CONSIST_URL_pre = False
for condition in trueCondition:
    if THROW_IF_MESSAGE_CONSIST_URL_ == condition:
        THROW_IF_MESSAGE_CONSIST_URL_pre = True
        break

DELETE_URL_FROM_MESSAGE_pre = False
for condition in trueCondition:
    if DELETE_URL_FROM_MESSAGE_ == condition:
        DELETE_URL_FROM_MESSAGE_pre = True
        break

outgoing = False
for condition in trueCondition:
    if FORWARD_FROM_YOUR_OWN_CHANNELS_ == condition:
        outgoing = True
        break

if len(FROM) == len(TO) and SEPARATE_CHANNELS:
    SEPARATE_CHANNELS = True
else:
    SEPARATE_CHANNELS = False

BLACKLIST_WORDS_ = BLACKLIST_WORDS_.strip()
if BLACKLIST_WORDS_.endswith(";"):
    BLACKLIST_WORDS_ = BLACKLIST_WORDS_.rstrip(BLACKLIST_WORDS_[-1])

if len(BLACKLIST_WORDS_) == 0:
    BLACKLIST_WORDS = []
else:
    BLACKLIST_WORDS = [str(i) for i in BLACKLIST_WORDS_.split(";")]

CHANGE_FOR_ = CHANGE_FOR_.strip()
if CHANGE_FOR_.endswith(";"):
    CHANGE_FOR_ = CHANGE_FOR_.rstrip(CHANGE_FOR_[-1])

if len(CHANGE_FOR_) == 0:
    CHANGE_FOR = []
else:
    CHANGE_FOR = [str(i) for i in CHANGE_FOR_.split(";")]

THROW_IF_MESSAGE_CONSIST_WORDS_ = THROW_IF_MESSAGE_CONSIST_WORDS_.strip()
if THROW_IF_MESSAGE_CONSIST_WORDS_.endswith(";"):
    THROW_IF_MESSAGE_CONSIST_WORDS_ = THROW_IF_MESSAGE_CONSIST_WORDS_.rstrip(
        THROW_IF_MESSAGE_CONSIST_WORDS_[-1])

if len(THROW_IF_MESSAGE_CONSIST_WORDS_) == 0:
    THROW_IF_MESSAGE_CONSIST_WORDS = []
else:
    THROW_IF_MESSAGE_CONSIST_WORDS = [
        str(i) for i in THROW_IF_MESSAGE_CONSIST_WORDS_.split(";")]

FORWARD_IF_MESSAGE_CONSIST_WORDS_ = FORWARD_IF_MESSAGE_CONSIST_WORDS_.strip()
if FORWARD_IF_MESSAGE_CONSIST_WORDS_.endswith(";"):
    FORWARD_IF_MESSAGE_CONSIST_WORDS_ = FORWARD_IF_MESSAGE_CONSIST_WORDS_.rstrip(
        FORWARD_IF_MESSAGE_CONSIST_WORDS_[-1])

if len(FORWARD_IF_MESSAGE_CONSIST_WORDS_) == 0:
    FORWARD_IF_MESSAGE_CONSIST_WORDS = []
else:
    FORWARD_IF_MESSAGE_CONSIST_WORDS = [
        str(i) for i in FORWARD_IF_MESSAGE_CONSIST_WORDS_.split(";")]

if THROW_IF_MESSAGE_CONSIST_URL_pre and not DELETE_URL_FROM_MESSAGE_pre:
    THROW_IF_MESSAGE_CONSIST_URL = True
    DELETE_URL_FROM_MESSAGE = False
elif not THROW_IF_MESSAGE_CONSIST_URL_pre and DELETE_URL_FROM_MESSAGE_pre:
    THROW_IF_MESSAGE_CONSIST_URL = False
    DELETE_URL_FROM_MESSAGE = True
else:
    THROW_IF_MESSAGE_CONSIST_URL = False
    DELETE_URL_FROM_MESSAGE = False
