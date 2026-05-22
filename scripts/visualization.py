import matplotlib.pyplot as plt
import seaborn as sns


def plot_confusion_matrix(matrix):

    plt.figure(figsize=(6, 4))

    sns.heatmap(

        matrix,

        annot=True,

        fmt='d',

        cmap='Blues'

    )

    plt.title(

        'Confusion Matrix'

    )

    plt.xlabel(

        'Predicted'

    )

    plt.ylabel(

        'Actual'

    )

    plt.tight_layout()

    plt.savefig(

        'outputs/confusion_matrix.png'

    )

    plt.close()