from model.distances import Distance


class SearchDto(object):

    def __init__(self, distance, numOfDocsToReturn, searchQuery, *args, **kwargs):
        self.distance = Distance.from_str(distance)
        self.numOfDocsToReturn = numOfDocsToReturn
        self.searchQuery = searchQuery
