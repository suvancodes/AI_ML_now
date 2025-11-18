import nltk

packages = [
    # Basic tokenizers
    "punkt",
    "punkt_tab",
    
    # Stopwords
    "stopwords",

    # Lemmatizer datasets
    "wordnet",
    "omw-1.4",

    # POS tagging
    "averaged_perceptron_tagger",
    "averaged_perceptron_tagger_eng",

    # Named Entity Recognition (NER)
    "maxent_ne_chunker",
    "words",

    # Stemming support (Snowball, Porter auto available)

    # Sentence + word tokenizers
    "punkt",
    "punkt_tab",

    # Chunking
    "conll2000",

    # Brown corpus (for model training)
    "brown",

    # Movie reviews sentiment dataset (for sentiment models)
    "movie_reviews",

    # Twitter tokenizer support
    "twitter_samples",

    # Gutenberg corpus (text dataset)
    "gutenberg",

    # Reuters corpus (text classification)
    "reuters",
]

for p in packages:
    print(f"Downloading: {p}")
    nltk.download(p)

