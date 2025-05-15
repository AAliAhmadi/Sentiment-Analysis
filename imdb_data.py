# imdb_data.py
from datasets import load_dataset, Dataset
import pandas as pd

def load_data(data_file=None):
    if data_file is None:
        # Default IMDB dataset
        dataset = load_dataset("imdb")
    else:
        # Load from user-provided file (expects one text entry per line)
        with open(data_file, "r", encoding="utf-8") as f:
            texts = [line.strip() for line in f if line.strip()]
        df = pd.DataFrame({"text": texts, "label": [0] * len(texts)})  # dummy labels for uniformity
        dataset = Dataset.from_pandas(df)
        dataset = {"train": dataset, "test": dataset}

    return dataset
