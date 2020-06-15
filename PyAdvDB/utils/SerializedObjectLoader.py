import os

import dill


def load_vectorizer():
    os.chdir('utils')
    vectorizer_filename = "vectorizer.dill"
    print('Reading \"' + vectorizer_filename + '\"')
    return dill.load(open(vectorizer_filename, 'rb'))
