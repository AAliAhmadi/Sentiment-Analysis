import argparse
from data import load_data
from model import load_model, predict_sentiment
from db import init_db, log_predictions

def main():
    parser = argparse.ArgumentParser(description="Sentiment analysis with BERT or spaCy + optional DB logging")
    parser.add_argument("--data_file", type=str, default=None, help="Optional path to a custom text file")
    parser.add_argument("--use_db", action="store_true", help="Log predictions to SQLite database")
    parser.add_argument("--backend", type=str, choices=["bert", "spacy"], default="bert", help="Choose backend model")
    args = parser.parse_args()

    dataset = load_data(args.data_file)
    texts = [d["text"] for d in dataset]

    # Load model
    if args.backend == "bert":
        tokenizer, model = load_model("bert")
        preds = predict_sentiment(texts, tokenizer, model=model, backend="bert")
    elif args.backend == "spacy":
        nlp = load_model("spacy")
        preds = predict_sentiment(texts, nlp, backend="spacy")
    else:
        raise ValueError(f"Unsupported backend: {args.backend}")


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
