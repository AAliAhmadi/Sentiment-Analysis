import torch
from transformers import BertTokenizer, BertForSequenceClassification

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

import torch
from transformers import BertTokenizer, BertForSequenceClassification

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

def load_model(backend="bert"):
    """
    Loads sentiment analysis model: 'bert' (default) or 'spacy'.
    """
    if backend == "spacy":
        nlp = spacy.load("en_core_web_sm")

        # Only add spacytextblob if not already added
        if "spacytextblob" not in nlp.pipe_names:
            nlp.add_pipe("spacytextblob")

        # Force register extension (to avoid error)
        if not spacy.tokens.Doc.has_extension("polarity"):
            spacy.tokens.Doc.set_extension("polarity", getter=lambda doc: doc._.blob.polarity)

        return nlp

    elif backend == "bert":
        tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        model = BertForSequenceClassification.from_pretrained("textattack/bert-base-uncased-imdb")
        model.eval()
        return tokenizer, model

    else:
        raise ValueError(f"Unknown backend: {backend}")


def predict_sentiment(texts, model_or_tokenizer, model=None, backend="bert"):
    """
    Predicts sentiment using the selected backend.
    - For BERT: model_or_tokenizer = tokenizer, model = BERT model
    - For spaCy: model_or_tokenizer = spaCy pipeline, model is ignored
    Returns a list of sentiments ("positive" or "negative").
    """
    sentiments = []

    if backend == "spacy":
        nlp = model_or_tokenizer
        for doc in nlp.pipe(texts, batch_size=32):
            if not doc.has_extension("polarity"):
                raise RuntimeError("Polarity extension not registered. Ensure 'spacytextblob' is added to the pipeline.")
            polarity = doc._.polarity
            sentiment = "positive" if polarity >= 0 else "negative"
            sentiments.append(sentiment)

    elif backend == "bert":
        tokenizer = model_or_tokenizer
        with torch.no_grad():
            for text in texts:
                inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
                outputs = model(**inputs)
                preds = torch.argmax(outputs.logits, dim=-1)
                sentiment = "positive" if preds.item() == 1 else "negative"
                sentiments.append(sentiment)

    else:
        raise ValueError(f"Unknown backend: {backend}")

    return sentiments
