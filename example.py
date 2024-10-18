# This example just connects to the WiFi network and
# runs a bot that will simply reply 'Ehi!' echoing what
# you just told it.

### Config your stuff here
Token =  "9283749392:HAF-Xd239cAAPOOpx9C7aFFzzAJrpo_EstE"
WifiNetwork = "MyNetwork"
WifiPassword = "mysecretpassword"
###

import uasyncio as asyncio
from telegram import TelegramBot

def mycallback(bot,msg_type,chat_name,sender_name,chat_id,text,entry):
    print(msg_type,chat_name,sender_name,chat_id,text)
    bot.send(chat_id,"Ehi! "+text)

bot = TelegramBot(Token,mycallback)
bot.connect_wifi(WifiNetwork, WifiPassword)
asyncio.create_task(bot.run())
loop = asyncio.get_event_loop()
loop.run_forever()
