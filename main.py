import argparse
from data import load_data
from model import load_model, predict_sentiment
from db import init_db, log_predictions

def main():
    parser = argparse.ArgumentParser(description="Sentiment analysis with BERT and SQLite logging")
    parser.add_argument("--data_file", type=str, default=None, help="Optional path to a custom text file")
    parser.add_argument("--use_db", action="store_true", help="Log predictions to SQLite database")
    args = parser.parse_args()

    # Load dataset (IMDB default or user file)
    dataset = load_data(args.data_file)
    texts = [d["text"] for d in dataset]

    # Load BERT model and tokenizer
    tokenizer, model = load_model()

    # Predict sentiments
    preds = predict_sentiment(texts, tokenizer, model)

    # Print predictions
    for text, pred in zip(texts, preds):
        print(f"Sentiment: {pred} | Text: {text[:60]}...")

    # Optional logging
    if args.use_db:
        init_db()
        log_predictions(texts, preds)
        print("Predictions logged to SQLite database.")

if __name__ == "__main__":
    main()
