import sqlite3

DB_FILE = "predictions.db"

def init_db():
    """
    Creates SQLite DB and table if not exist.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input_text TEXT NOT NULL,
            predicted_sentiment TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def log_predictions(texts, predictions):
    """
    Logs predictions into SQLite DB.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    for text, pred in zip(texts, predictions):
        c.execute("INSERT INTO predictions (input_text, predicted_sentiment) VALUES (?, ?)", (text, pred))
    conn.commit()
    conn.close()
