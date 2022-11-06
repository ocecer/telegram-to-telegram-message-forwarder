from env import *
from telethon import TelegramClient, events
from logging import basicConfig, WARNING
from telethon.sessions import StringSession
from urlextract import URLExtract

basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=WARNING)

print("Starting...")

try:
    BotUser = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
    BotUser.start()
except Exception as e:
    print(f"ERROR - {e}")
    exit(1)


@BotUser.on(events.NewMessage(outgoing=outgoing, incoming=True, chats=FROM))
async def sender_bH(event):
    # sender = await event.get_sender()
    # sender_id = sender.id
    peerUser = str(event.message.peer_id)
    sender_id = peerUser[peerUser.index("=")+1:len(peerUser)-1]
    userMessage = str(event.message.message)
    userMessage = checkMgs(userMessage)

    if len(userMessage) > 0:
        event.message.message = userMessage

        for i in range(len(TO)):
            if SEPARATE_CHANNELS:
                sendTo = find_index_of_channel(sender_id, FROM)

                try:
                    await BotUser.send_message(TO[sendTo], event.message)
                except Exception as e:
                    print(e)

                break
            else:
                try:
                    await BotUser.send_message(TO[i], event.message)
                except Exception as e:
                    print(e)


def find_index_of_channel(findIndexOf, findIndexIn):
    for i in range(len(findIndexIn)):
        if str(findIndexOf) in str(findIndexIn[i]):
            return i


def blacklistCheck(userMessage):
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

    if len(FORWARD_IF_MESSAGE_CONSIST_WORDS) > 0:
        found = False
        for word in FORWARD_IF_MESSAGE_CONSIST_WORDS:
            print(word)
            if word in userMessage:
                found = True
                userMessage = blacklistCheck(userMessage)
                break
            else:
                continue

        if not found:
            userMessage = ""

    else:
        userMessage = blacklistCheck(userMessage)

    return userMessage


print("Bot started.")
BotUser.run_until_disconnected()
