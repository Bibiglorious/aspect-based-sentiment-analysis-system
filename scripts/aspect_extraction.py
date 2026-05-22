def extract_unique_aspects(df):

    aspects = (

        df['aspect']

        .unique()

        .tolist()

    )

    print(

        'Extracted Aspects:'

    )

    print(aspects)

    return aspects