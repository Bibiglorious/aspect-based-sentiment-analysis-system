import nltk

from scripts.load_data import load_data

from scripts.preprocess import (
    preprocess_text
)

from scripts.feature_engineering import (
    vectorize_text
)

from scripts.train_model import (
    train_model
)

from scripts.evaluate_model import (
    evaluate_model
)

from scripts.visualization import (
    plot_confusion_matrix
)


nltk.download('punkt')
nltk.download('stopwords')


df = load_data()

df['cleaned_review'] = (

    df['review']

    .apply(preprocess_text)

)


X, vectorizer = vectorize_text(

    df['cleaned_review']

)


y = df['sentiment']


model, X_test, y_test = (

    train_model(X, y)

)


matrix = evaluate_model(

    model,

    X_test,

    y_test

)


plot_confusion_matrix(matrix)