1.	Open .env file and edit fields.
    a.	“APP_ID” and “API_HASH” - Can be found in https://my.telegram.org

    b.	 “SESSION” – Can be created from the following app. Run the app and follow instructions. https://replit.com/@TeamUltroid/UltroidStringSession

    c.	“FROM_CHANNEL” – Channel ID(s) of the channel(s) you will be forwarding messages from. If you will add more than 1 channel you should separate channel ID(s) with “;“.

    d.	“TO_CHANNEL” – Channel ID(s) of the channel(s) you will be forwarding messages to. If you will add more than 1 channel you should separate channel ID(s) with “;“. 

    e.	“SEPARATE_CHANNELS” – Enter 1 or 0. 
        i.	If you enter 1 bot will forward messages respectively
        Example: 1st FROM_CHANNEL to 1st TO_CHANNEL
        2nd FROM_CHANNEL to 2nd TO_CHANNEL
        3rd FROM_CHANNEL to 3rd TO_CHANNEL
        ii.	If you enter 0 bot will forward messages from all FROM_CHANNEL to all TO_CHANNEL
    
    f. "FORWARD_FROM_YOUR_OWN_CHANNELS" – Enter 1 or 0. If you enter 1 you can forward messages from your own channel to your own channel. 0, you cannot forward from your own channel.

    g.	“BLACKLIST_WORDS” – Enter blacklisted word(s) split by ";" or just one blacklist word.  

    h.	“CHANGE_FOR” – There are 3 ways to use CHANGE_FOR
        i.	If CHANGE_FOR will be empty, bot will delete all the BLACKLIST_WORDS from the message and forward.
        ii.	If you will enter one variable for CHANGE_FOR, bot will change all the BLACKLIST_WORDS from the messages as CHANGE_FOR and forward.
        iii.	If you will enter CHANGE_FOR for each BLACKLIST_WORDS, bot will change all the BLACKLIST_WORDS respectively with the CHANGE_FOR from the message and forward. (If you will not enter CHANGE_FOR for each BLACKLIST_WORDS, bot will just delete the BLACKLIST_WORDS. 
    
    i. "THROW_IF_MESSAGE_CONSIST_WORDS" – Enter word(s) split by ";" or just one word. If message consists any of the words defined here, the message will not be forwarded.

    k. "THROW_IF_MESSAGE_CONSIST_URL" – Enter 1 or 0. If you enter 1, bot will not forward the message if it contains any URL.

    k. "DELETE_URL_FROM_MESSAGE" – Enter 1 or 0. If you enter 1, bot will forward the message but URL(s) will be deleted from the message.

    ATTENTION: If you will enter 1 for the THROW_IF_MESSAGE_CONSIST_URL, DELETE_URL_FROM_MESSAGE should be 0, reversible. But if you will enter 0 or 1 for both THROW_IF_MESSAGE_CONSIST_URL and DELETE_URL_FROM_MESSAGE, the bot will not proccess URL(s)'s in the message and directly forward the URL(s).

2.	Clone the repo in your Heroku, CPanel or any any other platform where you can run a python app.
3.	Run: python3 bot.py
