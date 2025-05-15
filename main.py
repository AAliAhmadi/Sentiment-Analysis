from imdb_data import load_imdb
from model import SentimentModel
from database import SentimentDB

def main():
    dataset = load_imdb()
    model = SentimentModel()
    db = SentimentDB()

    for example in dataset:
        text = example["text"]
        sentiment = model.predict(text)
        db.insert_review(text, sentiment)

    db.close()
    print("Finished saving sentiments to SQLite DB")

if __name__ == "__main__":
    main()