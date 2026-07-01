import sqlite3

DB_NAME = "data.db"


def get_conn():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


conn = get_conn()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS messages (
    chat_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    message_id INTEGER NOT NULL
)
""")

conn.commit()


def save_message(chat_id: int, user_id: int, message_id: int):
    cur.execute(
        "INSERT INTO messages(chat_id, user_id, message_id) VALUES(?,?,?)",
        (chat_id, user_id, message_id)
    )
    conn.commit()


def get_messages(chat_id: int, user_id: int):
    cur.execute(
        "SELECT message_id FROM messages WHERE chat_id=? AND user_id=?",
        (chat_id, user_id)
    )
    return [row[0] for row in cur.fetchall()]


def clear_messages(chat_id: int, user_id: int):
    cur.execute(
        "DELETE FROM messages WHERE chat_id=? AND user_id=?",
        (chat_id, user_id)
    )
    conn.commit()
