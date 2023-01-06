from check_message import *
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from logging import basicConfig, WARNING

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
    sender = await event.get_sender()
    sender_id = sender.id
    userMessage = str(event.message.message)
    userMessage = checkMgs(userMessage)

    if userMessage != "THROW_THIS_MESSAGE":
        event.message.message = userMessage

        for i in range(len(TO)):
            if SEPARATE_CHANNELS:
                sendTo = find_index_of_channel(sender_id, FROM)

                try:
                    await BotUser.send_message(entity=TO[sendTo], message=event.message)
                except Exception as e:
                    print(e)

                break
            else:
                try:
                    await BotUser.send_message(entity=TO[i], message=event.message)
                except Exception as e:
                    print(e)
    else:
        print("Message thrown.")


def find_index_of_channel(findIndexOf, findIndexIn):
    for i in range(len(findIndexIn)):
        if str(findIndexOf) in str(findIndexIn[i]):
            return i


print("Bot started.")
BotUser.run_until_disconnected()
