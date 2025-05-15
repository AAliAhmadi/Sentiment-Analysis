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


2. Run with default IMDB test data:

```bash
python main.py

3. Run with your own text file:
```bash
python main.py --data_file your_text_file.txt

4. Log predictions to SQLite DB:
```bash
python main.py --use_db

or with your own file:

```bash
python main.py --data_file your_text_file.txt --use_db


### Files
- main.py: Main script with CLI interface

- data.py: Loads IMDB or custom text file data

- model.py: Loads BERT model and performs prediction

- db.py: SQLite database initialization and logging

- requirements.txt: Python packages

- README.md: This file


### Output
The script prints predictions for each text:

```bash
Sentiment: positive | Text: This movie was amazing with great acting...
Sentiment: negative | Text: I did not enjoy this film at all...

If logging is enabled, predictions are saved in predictions.db in table predictions.

### Notes
- The IMDB dataset is limited to 200 samples for demonstration speed.
- You can expand or modify the load_data function for other datasets.
- Requires internet connection the first time to download BERT and IMDB dataset.


