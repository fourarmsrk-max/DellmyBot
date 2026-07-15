import os

BOT_TOKEN = os.getenv("8940097553:AAHHeaxRwj4TTJwHUjZZsd4AMoiOWPjiZ_0")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable not found.")
