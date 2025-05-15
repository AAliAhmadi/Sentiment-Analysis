from datasets import load_dataset

def load_data(data_file=None):
    """
    Loads data from IMDB dataset (default) or a user-provided text file.
    Returns a list of dicts with key 'text'.
    """
    if data_file:
        dataset = []
        with open(data_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    dataset.append({"text": line})
        return dataset

    # Default IMDB dataset (only test split for speed)
    imdb = load_dataset("imdb", split="test[:200]")  # limit for demo speed
    dataset = [{"text": x["text"]} for x in imdb]
    return dataset
