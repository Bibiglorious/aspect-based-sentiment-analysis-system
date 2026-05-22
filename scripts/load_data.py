import xml.etree.ElementTree as ET
import pandas as pd


def load_data():

    tree = ET.parse(
        'data/raw/ABSA_TRAIN.xml'
    )

    root = tree.getroot()

    data = []

    for review in root.findall('Review'):

        sentences = review.find('sentences')

        if sentences is not None:

            for sentence in sentences.findall('sentence'):

                text = sentence.find('text')

                opinions = sentence.find('Opinions')

                if text is not None and opinions is not None:

                    for opinion in opinions.findall('Opinion'):

                        data.append({

                            'review': text.text,

                            'aspect': opinion.get('category'),

                            'sentiment': opinion.get('polarity')

                        })

    df = pd.DataFrame(data)

    return df