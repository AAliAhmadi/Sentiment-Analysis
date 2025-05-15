# Sentiment Analysis with BERT and SQLite Logging

## Overview
This project performs sentiment analysis on movie reviews using a pretrained BERT model.
You can analyze:
- The default IMDB test dataset (200 samples)
- Your own custom text file (one sentence per line)

Predictions can be optionally logged into a local SQLite database (`predictions.db`).

---

## Setup

1. Install dependencies (preferably in a virtual environment):

```bash
pip install -r requirements.txt
