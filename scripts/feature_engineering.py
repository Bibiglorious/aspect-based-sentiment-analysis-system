from sklearn.feature_extraction.text import TfidfVectorizer


def vectorize_text(train_text):

    vectorizer = TfidfVectorizer()

    X = vectorizer.fit_transform(
        train_text
    )

    return X, vectorizer