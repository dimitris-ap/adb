from flask import jsonify

from model.distances import Distance
from model.document_dto import DocumentDto
from model.relevantdocsresponsedto import RelevantDocsResponseDto
from utils.DistanceUtils import calc_euclidean, calc_city_block, calc_canberra, calc_chebyshev, calc_minkowski, \
    calc_kulczynski
from utils.PreprocessUtils import preprocess_single_query
from utils.SerializedObjectLoader import load_vectorizer

vectorizer = load_vectorizer()


def get_relevant_docs(query_vec, num_of_docs, distance):
    if distance == Distance.EUCLIDEAN:
        most_relevant_df = calc_euclidean(query_vec, num_of_docs)
    elif distance == Distance.CITY_BLOCK:
        most_relevant_df = calc_city_block(query_vec, num_of_docs)
    elif distance == Distance.CANBERRA:
        most_relevant_df = calc_canberra(query_vec, num_of_docs)
    elif distance == Distance.CHEBYSHEV:
        most_relevant_df = calc_chebyshev(query_vec, num_of_docs)
    elif distance == Distance.MINKOWSKI:
        most_relevant_df = calc_minkowski(query_vec, num_of_docs)
    elif distance == Distance.KULCZYNSKI:
        most_relevant_df = calc_kulczynski(query_vec, num_of_docs)
    else:
        raise Exception("Unsupported distance!")

    # Converting dataframe with the most relevant documets
    # into an array with Document objects
    relevant_documents = []
    for index, row in most_relevant_df.iterrows():
        filename = row['filename']
        path = row['path']
        with open(path + filename, 'r') as f:
            content = f.read()
            title = content.split('\n')[0]
            sample = content[0:200]  # first 200 chars - just for sampling the text file
            relevant_documents.append(DocumentDto(path=path, filename=filename, content=content, sample=sample, title=title))
    return relevant_documents


def search_for(search_dto):
    preprocessed_query_vec = preprocess_single_query(vectorizer, search_dto.searchQuery)

    docs = get_relevant_docs(query_vec=preprocessed_query_vec,
                             num_of_docs=search_dto.numOfDocsToReturn,
                             distance=search_dto.distance)

    rel_docs = RelevantDocsResponseDto(documents=[d.serialize() for d in docs])
    return jsonify(rel_docs.__dict__)
