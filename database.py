import sqlite3

class SentimentDB:
    def __init__(self, db_path="imdb_sentiment.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            sentiment INTEGER NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_review(self, text, sentiment):
        query = "INSERT INTO reviews (text, sentiment) VALUES (?, ?)"
        self.conn.execute(query, (text, sentiment))
        self.conn.commit()

    def close(self):
        self.conn.close()