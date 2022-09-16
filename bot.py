from telethon import TelegramClient, events
from decouple import config
from logging import basicConfig, WARNING
from telethon.sessions import StringSession

basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=WARNING)

print("Starting...")

# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
SESSION = config("SESSION")
FROM_ = config("FROM_CHANNEL")
TO_ = config("TO_CHANNEL")
SEPARATE_CHANNELS = config("SEPARATE_CHANNELS")
BLACKLIST_WORDS_ = config("BLACKLIST_WORDS")
CHANGE_FOR_ = config("CHANGE_FOR")

FROM = [int(i) for i in FROM_.split(";")]
TO = [int(i) for i in TO_.split(";")]

if len(FROM) == len(TO) and SEPARATE_CHANNELS == "1":
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

try:
    BotzHubUser = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
    BotzHubUser.start()
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

if SEPARATE_CHANNELS:
    for i in range(len(FROM)):
        @BotzHubUser.on(events.NewMessage(incoming=True, chats=FROM[i]))
        async def sender_bH(event):

            if len(BLACKLIST_WORDS) > 0:
                userMessage = str(event.message.message)
                userMessage = checkMgs(
                    BLACKLIST_WORDS, CHANGE_FOR, userMessage)
                event.message.message = userMessage

            try:
                await BotzHubUser.send_message(
                    TO[i],
                    event.message
                )
            except Exception as e:
                print(e)

else:
    @BotzHubUser.on(events.NewMessage(incoming=True, chats=FROM))
    async def sender_bH(event):

        if len(BLACKLIST_WORDS) > 0:
            userMessage = str(event.message.message)
            userMessage = checkMgs(
                BLACKLIST_WORDS, CHANGE_FOR, userMessage)
            event.message.message = userMessage

        for i in TO:
            try:
                await BotzHubUser.send_message(
                    i,
                    event.message
                )
            except Exception as e:
                print(e)


def checkMgs(blacklist, changeFor, userMessage):
    if len(changeFor) == 0:
        for word in blacklist:
            if word in userMessage:
                userMessage = userMessage.replace(word, "")
    elif len(blacklist) >= 1 and len(changeFor) == 1:
        for word in blacklist:
            if word in userMessage:
                userMessage = userMessage.replace(word, changeFor[0])
    else:
        if len(blacklist) == len(changeFor):
            for i in range(len(blacklist)):
                word = blacklist[i]
                if word in userMessage:
                    userMessage = userMessage.replace(word, changeFor[i])
        else:
            for word in blacklist:
                if word in userMessage:
                    userMessage = userMessage.replace(word, "")

    return userMessage


print("Bot has started.")
BotzHubUser.run_until_disconnected()
