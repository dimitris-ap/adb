import numpy as np
from scipy.spatial.distance import cityblock, minkowski, canberra, kulsinski, chebyshev

from utils.DBUtils import load_data_from_db

print("Loading documents from db...")
data = load_data_from_db()
print("Done!")


def calc_euclidean(query_vec, num_of_docs):  # smaller better!
    vec_distances = []
    for index, row in data.iterrows():
        vec_distances.append(np.linalg.norm(query_vec.toarray() - row['text']))

    result_docs = data.copy()
    result_docs['euclidean'] = list(vec_distances)
    result_docs = result_docs.sort_values(by=['euclidean'])  # default: asc

    result_docs = result_docs.head(num_of_docs)
    result_docs.drop('euclidean', axis=1, inplace=True)
    return result_docs


def calc_city_block(query_vec, num_of_docs):  # smaller better!
    vec_distances = []
    for index, row in data.iterrows():
        vec_distances.append(cityblock(query_vec.toarray(), row['text']))

    result_docs = data.copy()
    result_docs['cityblock'] = list(vec_distances)
    result_docs = result_docs.sort_values(by=['cityblock'])  # default: asc

    result_docs = result_docs.head(num_of_docs)
    result_docs.drop('cityblock', axis=1, inplace=True)
    return result_docs


def calc_canberra(query_vec, num_of_docs):  # bigger better
    vec_distances = []
    for index, row in data.iterrows():
        vec_distances.append(canberra(query_vec.toarray(), row['text']))

    result_docs = data.copy()
    result_docs['canberra'] = list(vec_distances)
    result_docs = result_docs.sort_values(by=['canberra'], ascending=False)  # default: asc

    result_docs = result_docs.head(num_of_docs)
    result_docs.drop('canberra', axis=1, inplace=True)
    return result_docs


def calc_chebyshev(query_vec, num_of_docs):  # bigger better
    vec_distances = []
    for index, row in data.iterrows():
        vec_distances.append(chebyshev(query_vec.toarray(), row['text']))

    result_docs = data.copy()
    result_docs['chebyshev'] = list(vec_distances)
    result_docs = result_docs.sort_values(by=['chebyshev'], ascending=False)  # default: asc

    result_docs = result_docs.head(num_of_docs)
    result_docs.drop('chebyshev', axis=1, inplace=True)
    return result_docs


def calc_minkowski(query_vec, num_of_docs):  # smaller better!
    vec_distances = []
    for index, row in data.iterrows():
        vec_distances.append(minkowski(query_vec.toarray(), row['text']))

    result_docs = data.copy()
    result_docs['minkowski'] = list(vec_distances)
    result_docs = result_docs.sort_values(by=['minkowski'])  # default: asc

    result_docs = result_docs.head(num_of_docs)
    result_docs.drop('minkowski', axis=1, inplace=True)
    return result_docs


def calc_kulczynski(query_vec, num_of_docs):  # smaller better!
    vec_distances = []
    for index, row in data.iterrows():
        vec_distances.append(kulsinski(query_vec.toarray(), row['text']))

    result_docs = data.copy()
    result_docs['kulsinski'] = list(vec_distances)
    result_docs = result_docs.sort_values(by=['kulsinski'])  # default: asc

    result_docs = result_docs.head(num_of_docs)
    result_docs.drop('kulsinski', axis=1, inplace=True)
    return result_docs
