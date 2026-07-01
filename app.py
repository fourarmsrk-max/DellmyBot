import os
import threading
from flask import Flask
from bot import run_bot

app = Flask(__name__)

@app.route("/")
def home():
    return "DeleteMy Bot is Running!"

def start_bot():
    run_bot()

threading.Thread(target=start_bot, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
