import re


def clean_text(text):
    """
    Clean financial news or social media text
    for NLP processing.
    """

    if not isinstance(text, str):
        return ""

    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove special characters and punctuation
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


if __name__ == "__main__":
    sample_text = "Alpha Motors reports STRONG growth!!! Investors are optimistic."

    cleaned = clean_text(sample_text)

    print("Original:")
    print(sample_text)

    print("\nCleaned:")
    print(cleaned)