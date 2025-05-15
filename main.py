from model import SentimentModel
from database import SentimentDB
import argparse
from imdb_data import load_data  # or wherever your load_data function is


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_file", type=str, default=None, help="Optional path to a custom text file")
    args = parser.parse_args()

    dataset = load_data(args.data_file)  # Use user-provided file or IMDB
    
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
