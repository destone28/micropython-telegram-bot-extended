This code implements a very simple non-blocking Telegram bot library
for MicroPython based MCUs such as the ESP32 and similar microcontrollers.

Quick facts about how this can be useful and how it is implemented:

* **What you can do with this code?** You can implement bots that run into microcontrollers so that you can control your projects / IoT devices via Telegram.
* **What the library implements?** It calls your callback when the bot receives a message, and then you have an API to send messages. Just that. No advanced features are supported.
* **This implementation has limits.** The code uses non blocking sockets. It cut corners in order to be simple and use few memory, it may break, it's not a technically super "sane" implementation, but it is extremely easy to understand and modify.
* The code is BSD licensed.
* The MicroPython JSON library does not translate surrogate UTF-16 characters, so this library implements a quick and dirty conversion to UTF-8.

## How to test it?

1. Create your bot using the Telegram [@BotFather](https://t.me/botfather).
2. After obtaining your bot API key, edit the `example.py` file and put there your API key (also called *token*). Make sure to also put your WiFi credentials, as the microcontroller needs to connect to the Internet for this to work.
3. Put the `telegram.py` file into the device flash memory with:

    mp cp telegram.py :

4. Execute the example with:

    mp run example.y

5. Talk to your bot. It will echo what you write to it.
6. If your bot is inside a group, make sure to give it admin privileges, otherwise it will be unable to get messages.

## How to use the API?

Run the bot in its own coroutine with:


```python
bot = TelegramBot(Token,mycallback)
bot.connect_wifi(WifiNetwork, WifiPassword)
asyncio.create_task(bot.run())
loop = asyncio.get_event_loop()
loop.run_forever()
```

The callback looks like that:


```python
def mycallback(bot,msg_type,chat_name,sender_name,chat_id,text,entry):
    print(msg_type,chat_name,sender_name,chat_id,text)
    bot.send(sender_id,"Ehi! "+text)
```

The arguments it receives are:

* `msg_type` is private, group, supergroup, channel, depending on the entity that sent us the message.
* `chat_name` Group/Channel name if the message is not a private message. Otherwise `None`.
* `sender_name` is the Telegram username of the caller, or the name of the group/channel.
* `chat_id` is the Telegram ID of the user/chat: this ID is specific of the user/group/channel. You need to use this ID with the `.send()` method to reply in the same place the message arrived to you.
* `text` is the content of the message. UTF-8 encoded.
* `entry` is the raw JSON entry received from Telegram. From there you can take all the other stuff not directly passed to the function.

The only method you can call is `.send()`, with the ID of the recipient and your text message. A third optional argument called **glue** can be `True` or `False`. By default it is `False`. When it is `True`, messages having the same target ID as the previous message are *glued* together, up to 2k of text, so we can avoid sending too many messages via the API.
