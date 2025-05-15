# 🧠 Sentiment Analyzer (BERT or spaCy)

A modular Python tool for performing **sentiment analysis** on either the [IMDB dataset](https://huggingface.co/datasets/imdb) or your **custom text input** using:

- 🤗 **BERT** via HuggingFace Transformers for high-accuracy predictions.
- ⚡ **spaCy** (with `spacytextblob`) for fast, lightweight inference.

Predictions can optionally be saved to a local **SQLite** database for tracking.

---

## 📦 Features

- 🔀 Switch between `bert` and `spacy` backends.
- 📁 Accepts either the IMDB test set or a user-provided `.txt` file.
- 🧾 Logs predictions to an SQLite database (`predictions.db`) when enabled.
- 🧼 Simple, modular design: `data.py`, `model.py`, `db.py`, `main.py`.

---

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/AAliAhmadi/Sentiment-Analysi.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) If using spacy, ensure the English model is downloaded:

    ```bash
    python -m spacy download en_core_web_sm
    ```

## 🚀 Usage
### 📊 Analyze IMDB test data (default)
```bash
python main.py --backend bert
```
### 📄 Analyze your own text file
```bash
python main.py --data_file my_texts.txt --backend spacy
```

Your file should be a plain .txt file with one sentence or paragraph per line.

Example `my_texts.txt`:
```css
I loved the acting and the story.
This was a terrible movie. Waste of time.
```

### 🗃️ Log predictions to SQLite database
```bash
python main.py --backend bert --use_db
```
The database file `predictions.db` will be created (if it doesn't exist), and predictions will be stored in a table named predictions.

### 🧾 Output Example
Sample console output:

```
Sentiment: positive | Text: I love sci-fi and am willing to put up with a lot. Sci-fi mo...
Sentiment: positive | Text: Worth the entertainment value of a rental, especially if you...
Sentiment: negative | Text: its a totally average film with a few semi-alright action se...
Sentiment: positive | Text: STAR RATING: ***** Saturday Night **** Friday Night *** Frid...
Sentiment: positive | Text: First off let me say, If you haven't enjoyed a Van Damme mov...
Sentiment: positive | Text: I had high hopes for this one until they changed the name to...
Sentiment: positive | Text: Isaac Florentine has made some of the best western Martial A...
Sentiment: negative | Text: It actually pains me to say it, but this movie was horrible ...
Sentiment: negative | Text: Technically I'am a Van Damme Fan, or I was. this movie is so...
Sentiment: negative | Text: Honestly awful film, bad editing, awful lighting, dire dialo...
```

### Sample database row (from predictions.db):

| id | input\_text                               | predicted\_sentiment |
| -- | ----------------------------------------- | -------------------- |
| 1  | This was a terrible movie. Waste of time. | negative             |


## 🧩 Project Structure

```
├── data.py         # Load IMDB or custom text data
├── db.py           # SQLite initialization and logging
├── model.py        # Load BERT or spaCy model + prediction logic
├── main.py         # Main runner script with CLI args
├── requirements.txt
└── README.md
```

## 📜 License
MIT License. Feel free to use, extend, or contribute!




