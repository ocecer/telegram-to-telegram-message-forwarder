from env import *
from telethon import TelegramClient, events
from logging import basicConfig, WARNING
from telethon.sessions import StringSession
from urlextract import URLExtract

basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=WARNING)

print("Starting...")

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
            userMessage = str(event.message.message)
            userMessage = checkMgs(userMessage)
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
        userMessage = str(event.message.message)
        userMessage = checkMgs(userMessage)
        event.message.message = userMessage

        for i in TO:
            try:
                await BotzHubUser.send_message(
                    i,
                    event.message
                )
            except Exception as e:
                print(e)


def checkMgs(userMessage):

    if THROW_IF_MESSAGE_CONSIST_URL:
        urlExtract = URLExtract()
        urls = urlExtract.find_urls(userMessage)

        if len(urls) > 0:
            userMessage = ""
            return userMessage
       
    if len(THROW_IF_MESSAGE_CONSIST_WORDS) > 0:
        for word in THROW_IF_MESSAGE_CONSIST_WORDS:
            if word in userMessage:
                userMessage = ""
                return userMessage

    if DELETE_URL_FROM_MESSAGE:
        urlExtract = URLExtract()
        urls = urlExtract.find_urls(userMessage)

        if len(urls) > 0:
            for url in urls:
                if url in userMessage:
                    userMessage = userMessage.replace(url, "")
        
    if len(BLACKLIST_WORDS) > 0:
        if len(CHANGE_FOR) == 0:
            for word in BLACKLIST_WORDS:
                if word in userMessage:
                    userMessage = userMessage.replace(word, "")
        elif len(BLACKLIST_WORDS) >= 1 and len(CHANGE_FOR) == 1:
            for word in BLACKLIST_WORDS:
                if word in userMessage:
                    userMessage = userMessage.replace(word, CHANGE_FOR[0])
        else:
            if len(BLACKLIST_WORDS) == len(CHANGE_FOR):
                for i in range(len(BLACKLIST_WORDS)):
                    word = BLACKLIST_WORDS[i]
                    if word in userMessage:
                        userMessage = userMessage.replace(word, CHANGE_FOR[i])
            else:
                for word in BLACKLIST_WORDS:
                    if word in userMessage:
                        userMessage = userMessage.replace(word, "")
 
    return userMessage


print("Bot has started.")
BotzHubUser.run_until_disconnected()
