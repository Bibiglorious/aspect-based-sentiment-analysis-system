from sklearn.metrics import (

    classification_report,

    confusion_matrix,

    accuracy_score

)


def evaluate_model(

    model,

    X_test,

    y_test

):

    predictions = model.predict(X_test)

    accuracy = accuracy_score(

        y_test,

        predictions

    )

    matrix = confusion_matrix(

        y_test,

        predictions

    )

    report = classification_report(

        y_test,

        predictions

    )

    print(

        'Accuracy:',

        accuracy

    )

    print(report)

    return matrix