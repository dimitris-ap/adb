import os

import pandas as pd

from utils.PreprocessUtils import clean_text, remove_stopwords, lemmatize_text, tf_idf, export_tfidf_to_dill


def files_to_df():
    path = '..\\data\\bbc'
    # path = '..\\data\\bbcSample'
    df = pd.DataFrame(columns=['id', 'path', 'filename', 'text'])
    for root, dirs, files in os.walk(path):
        for file in files:
            identifier = len(df)
            path = os.path.abspath(root) + os.path.sep
            filename = file
            text = open(path + filename, "r").read()
            df.loc[identifier] = [identifier, path, filename, text]

    return df


def initialize():
    print('Loading data...')
    data = files_to_df()  # ['id', 'path', 'filename', 'text']

    print('Data cleansing...')
    data.text = data.text.apply(lambda x: clean_text(x))
    data.text = data.text.apply(lambda x: remove_stopwords(x))
    data.text = data.text.apply(lambda x: lemmatize_text(x))
    print('Data cleaned!')

    return tf_idf(data)
