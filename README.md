This code implements a very simple non-blocking Telegram bot library
for MicroPython based MCUs such as the ESP32 and similar microcontrollers.

Quick facts about how this can be useful and how it is implemented:

* **What you can do with this code?** You can implement bots that run into microcontrollers so that you can control your projects / IoT devices via Telegram.
* **What the library implements?** It calls your callback when the bot receives a message, and then you have an API to send messages. Just that. No advanced features are supported.
* **This implementation has limits.** The code uses non blocking sockets. It cut corners in order to be simple and use few memory, it may break, it's not a technically super "sane" implementation, but it is extremely easy to understand and modify.
* The code is BSD licensed.
* The MicroPython JSON library does not translate surrogate UTF-16 characters, so this library implements a quick and dirty conversion to UTF-8.

## How to use it?

1. Create your bot using the Telegram [@BotFather](https://t.me/botfather).
2. After obtaining your bot API key, edit the `example.py` file and put there your API key (also called *token*). Make sure to also put your WiFi credentials, as the microcontroller needs to connect to the Internet for this to work.
3. Put the `telegram.py` file into the device flash memory with:

    mp cp telegram.py :

4. Execute the example with:

    mp run example.y

5. Talk to your bot. It will echo what you write to it.
