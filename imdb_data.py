from datasets import load_dataset

def load_imdb(split="test[:100]"):
    dataset = load_dataset("imdb", split=split)
    return dataset