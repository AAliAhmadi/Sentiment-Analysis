import torch
from transformers import BertTokenizer, BertForSequenceClassification

def load_model():
    """
    Loads BERT tokenizer and model for sentiment classification.
    """
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = BertForSequenceClassification.from_pretrained("textattack/bert-base-uncased-imdb")
    model.eval()
    return tokenizer, model

def predict_sentiment(texts, tokenizer, model):
    """
    Predicts sentiment (positive/negative) for a list of texts.
    Returns a list of sentiment strings.
    """
    sentiments = []
    with torch.no_grad():
        for text in texts:
            inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
            outputs = model(**inputs)
            preds = torch.argmax(outputs.logits, dim=-1)
            sentiment = "positive" if preds.item() == 1 else "negative"
            sentiments.append(sentiment)
    return sentiments
