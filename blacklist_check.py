from env import *


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
