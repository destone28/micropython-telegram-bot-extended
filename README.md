# MicroPython Telegram Bot for IoT Devices

A lightweight, memory-efficient Telegram Bot implementation for MicroPython-enabled IoT devices with media capabilities. This library is particularly optimized for Arduino devices running MicroPython, such as Arduino Nicla Vision.

This project is a fork of [micropython-telegram-bot](https://github.com/antirez/micropython-telegram-bot) by Salvatore Sanfilippo, with extended functionality for IoT surveillance applications.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [Advanced Features](#advanced-features)
- [Media Capabilities](#media-capabilities)
- [Examples](#examples)
- [Nicla Vision Integration](#nicla-vision-integration)
- [License](#license)
- [Versione Italiana](#versione-italiana)

## Features

- Extremely lightweight implementation optimized for MicroPython devices with limited resources
- Reliable connection management with automatic reconnection
- Support for sending and receiving text messages
- Advanced media capabilities:
  - Send photos (JPEG)
  - Send videos (MJPEG)
- Callback-based message handling
- User authorization system
- Queue management for outgoing messages
- WiFi connection helper

## Installation

1. Ensure you have MicroPython installed on your device (version 1.19 or higher recommended)
2. Copy `telegram.py` to your device's filesystem
   - With Arduino Lab for MicroPython: Use the file manager to upload the file
   - With `mpremote`: Run `mpremote cp telegram.py :`

## Basic Usage

```python
import uasyncio as asyncio
from telegram import TelegramBot

# Your Telegram bot token (get it from @BotFather)
BOT_TOKEN = "your_bot_token"

# Define your message handler
def message_handler(bot, msg_type, chat_name, sender_name, chat_id, text, message_object):
    print(f"Message from {sender_name}: {text}")
    
    # Reply to the message
    if text == "/start":
        bot.send(chat_id, "Hello! I'm your IoT bot.")
    elif text == "/status":
        bot.send(chat_id, "System is running normally.")

# Create the bot
bot = TelegramBot(BOT_TOKEN, message_handler)

# Optional: Connect to WiFi
bot.connect_wifi("your_wifi_ssid", "your_wifi_password")

# Initialize the async event loop
loop = asyncio.get_event_loop()

# Start the bot
asyncio.create_task(bot.run())

# Run other tasks as needed
# ...

# Run the event loop
loop.run_forever()
```

## Advanced Features

### User Authorization

You can restrict access to your bot by implementing an authorization system:

```python
# List of authorized user IDs
AUTHORIZED_USERS = ["123456789", "987654321"]

def is_authorized(chat_id):
    return str(chat_id) in AUTHORIZED_USERS

def message_handler(bot, msg_type, chat_name, sender_name, chat_id, text, message_object):
    if not is_authorized(chat_id):
        bot.send(chat_id, "Unauthorized access.")
        return
    
    # Process authorized messages
    # ...
```

### Message Queuing

The bot automatically queues outgoing messages to ensure reliable delivery even during network issues.

## Media Capabilities

### Sending Photos

```python
# Capture a photo (device-specific implementation)
# ...

# Save the photo
photo_path = "photo.jpg"

# Send the photo
bot.send_photo(chat_id, photo_path, "Photo caption")
```

### Sending Videos

```python
# Record a video (device-specific implementation)
# ...

# Save the video
video_path = "video.mjpeg"

# Send the video
bot.send_video(chat_id, video_path, "Video caption")
```

## Examples

### Command Handler System

```python
def message_handler(bot, msg_type, chat_name, sender_name, chat_id, text, message_object):
    if text == "/photo":
        bot.send(chat_id, "Taking a photo...")
        # Device-specific photo capture code
        # ...
        photo_path = "captured_photo.jpg"
        bot.send_photo(chat_id, photo_path, "Here's your photo")
    
    elif text == "/video":
        bot.send(chat_id, "Recording a video...")
        # Device-specific video recording code
        # ...
        video_path = "captured_video.mjpeg"
        bot.send_video(chat_id, video_path, "Here's your video")
```

## Nicla Vision Integration

This library is optimized for use with Arduino Nicla Vision and similar devices. Integration examples:

```python
# Import device-specific libraries
import sensor
import mjpeg

# Initialize the camera
def init_camera():
    sensor.reset()
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
    sensor.skip_frames(time=2000)
    return True

# Capture a photo
def capture_photo(filename):
    img = sensor.snapshot()
    img.save(filename, quality=90)
    return filename

# Record a video
def record_video(filename, duration=5, fps=10):
    video = mjpeg.Mjpeg(filename)
    start_time = time.time()
    
    while time.time() - start_time < duration:
        img = sensor.snapshot()
        video.write(img, quality=50)
        time.sleep(1/fps)
    
    video.close()
    return filename

# Telegram bot handler for Nicla Vision
def message_handler(bot, msg_type, chat_name, sender_name, chat_id, text, message_object):
    if text == "/photo":
        init_camera()
        photo_path = capture_photo("telegram_photo.jpg")
        bot.send_photo(chat_id, photo_path, "Photo from Nicla Vision")
    
    elif text == "/video":
        init_camera()
        video_path = record_video("telegram_video.mjpeg")
        bot.send_video(chat_id, video_path, "Video from Nicla Vision")
```

## License

This project uses dual licensing:
- Original micropython-telegram-bot code by Salvatore Sanfilippo is under BSD 2-clause license
- Added extensions and examples are under AGPL-3.0 license

See the [LICENSE](LICENSE) file for details.

---

# Versione Italiana

# MicroPython Telegram Bot per Dispositivi IoT

Un'implementazione leggera ed efficiente di un bot Telegram per dispositivi IoT con MicroPython e capacità multimediali. Questa libreria è particolarmente ottimizzata per dispositivi Arduino con MicroPython, come Arduino Nicla Vision.

Questo progetto è un fork di [micropython-telegram-bot](https://github.com/antirez/micropython-telegram-bot) di Salvatore Sanfilippo, con funzionalità estese per applicazioni di videosorveglianza IoT.

## Indice

- [Caratteristiche](#caratteristiche)
- [Installazione](#installazione)
- [Utilizzo Base](#utilizzo-base)
- [Funzionalità Avanzate](#funzionalità-avanzate)
- [Capacità Multimediali](#capacità-multimediali)
- [Esempi](#esempi)
- [Integrazione con Nicla Vision](#integrazione-con-nicla-vision)
- [Licenza](#licenza)

## Caratteristiche

- Implementazione estremamente leggera ottimizzata per dispositivi MicroPython con risorse limitate
- Gestione affidabile della connessione con riconnessione automatica
- Supporto per invio e ricezione di messaggi di testo
- Capacità multimediali avanzate:
  - Invio di foto (JPEG)
  - Invio di video (MJPEG)
- Gestione dei messaggi basata su callback
- Sistema di autorizzazione utenti
- Gestione delle code per i messaggi in uscita
- Helper per la connessione WiFi

## Installazione

1. Assicurati di avere MicroPython installato sul tuo dispositivo (versione 1.19 o superiore consigliata)
2. Copia `telegram.py` nel filesystem del tuo dispositivo
   - Con Arduino Lab for MicroPython: Usa il file manager per caricare il file
   - Con `mpremote`: Esegui `mpremote cp telegram.py :`

## Utilizzo Base

```python
import uasyncio as asyncio
from telegram import TelegramBot

# Il tuo token del bot Telegram (ottenilo da @BotFather)
BOT_TOKEN = "il_tuo_token"

# Definisci il tuo gestore di messaggi
def gestore_messaggi(bot, tipo_msg, nome_chat, nome_mittente, id_chat, testo, oggetto_messaggio):
    print(f"Messaggio da {nome_mittente}: {testo}")
    
    # Rispondi al messaggio
    if testo == "/start":
        bot.send(id_chat, "Ciao! Sono il tuo bot IoT.")
    elif testo == "/stato":
        bot.send(id_chat, "Il sistema sta funzionando normalmente.")

# Crea il bot
bot = TelegramBot(BOT_TOKEN, gestore_messaggi)

# Opzionale: Connettiti al WiFi
bot.connect_wifi("nome_rete_wifi", "password_wifi")

# Inizializza il loop di eventi asincrono
loop = asyncio.get_event_loop()

# Avvia il bot
asyncio.create_task(bot.run())

# Esegui altri task se necessario
# ...

# Esegui il loop di eventi
loop.run_forever()
```

## Funzionalità Avanzate

### Autorizzazione Utenti

Puoi limitare l'accesso al tuo bot implementando un sistema di autorizzazione:

```python
# Lista di ID utenti autorizzati
UTENTI_AUTORIZZATI = ["123456789", "987654321"]

def è_autorizzato(id_chat):
    return str(id_chat) in UTENTI_AUTORIZZATI

def gestore_messaggi(bot, tipo_msg, nome_chat, nome_mittente, id_chat, testo, oggetto_messaggio):
    if not è_autorizzato(id_chat):
        bot.send(id_chat, "Accesso non autorizzato.")
        return
    
    # Elabora i messaggi autorizzati
    # ...
```

### Code di Messaggi

Il bot mette automaticamente in coda i messaggi in uscita per garantire una consegna affidabile anche durante problemi di rete.

## Capacità Multimediali

### Invio di Foto

```python
# Cattura una foto (implementazione specifica del dispositivo)
# ...

# Salva la foto
percorso_foto = "foto.jpg"

# Invia la foto
bot.send_photo(id_chat, percorso_foto, "Didascalia della foto")
```

### Invio di Video

```python
# Registra un video (implementazione specifica del dispositivo)
# ...

# Salva il video
percorso_video = "video.mjpeg"

# Invia il video
bot.send_video(id_chat, percorso_video, "Didascalia del video")
```

## Esempi

### Sistema di Gestione Comandi

```python
def gestore_messaggi(bot, tipo_msg, nome_chat, nome_mittente, id_chat, testo, oggetto_messaggio):
    if testo == "/foto":
        bot.send(id_chat, "Sto scattando una foto...")
        # Codice specifico per la cattura della foto
        # ...
        percorso_foto = "foto_catturata.jpg"
        bot.send_photo(id_chat, percorso_foto, "Ecco la tua foto")
    
    elif testo == "/video":
        bot.send(id_chat, "Sto registrando un video...")
        # Codice specifico per la registrazione del video
        # ...
        percorso_video = "video_registrato.mjpeg"
        bot.send_video(id_chat, percorso_video, "Ecco il tuo video")
```

## Integrazione con Nicla Vision

Questa libreria è ottimizzata per l'uso con Arduino Nicla Vision e dispositivi simili. Esempi di integrazione:

```python
# Importa librerie specifiche del dispositivo
import sensor
import mjpeg

# Inizializza la fotocamera
def inizializza_fotocamera():
    sensor.reset()
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
    sensor.skip_frames(time=2000)
    return True

# Cattura una foto
def cattura_foto(nome_file):
    img = sensor.snapshot()
    img.save(nome_file, quality=90)
    return nome_file

# Registra un video
def registra_video(nome_file, durata=5, fps=10):
    video = mjpeg.Mjpeg(nome_file)
    tempo_inizio = time.time()
    
    while time.time() - tempo_inizio < durata:
        img = sensor.snapshot()
        video.write(img, quality=50)
        time.sleep(1/fps)
    
    video.close()
    return nome_file

# Gestore del bot Telegram per Nicla Vision
def gestore_messaggi(bot, tipo_msg, nome_chat, nome_mittente, id_chat, testo, oggetto_messaggio):
    if testo == "/foto":
        inizializza_fotocamera()
        percorso_foto = cattura_foto("foto_telegram.jpg")
        bot.send_photo(id_chat, percorso_foto, "Foto da Nicla Vision")
    
    elif testo == "/video":
        inizializza_fotocamera()
        percorso_video = registra_video("video_telegram.mjpeg")
        bot.send_video(id_chat, percorso_video, "Video da Nicla Vision")
```

## Licenza

Questo progetto utilizza una doppia licenza:
- Il codice originale micropython-telegram-bot di Salvatore Sanfilippo è sotto licenza BSD 2-clause
- Le estensioni e gli esempi aggiunti sono sotto licenza AGPL-3.0

Vedi il file [LICENSE](LICENSE) per i dettagli.
