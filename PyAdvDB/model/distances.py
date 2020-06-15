from enum import Enum


class Distance(Enum):
    EUCLIDEAN = "Euclidean"
    CITY_BLOCK = "City Block"
    MINKOWSKI = "Minkowski"
    CHEBYSHEV = "Chebyshev"
    KULCZYNSKI = "Kulczynski"
    CANBERRA = "Canberra"

    @staticmethod
    def from_str(value) -> Enum:
        for m, mm in Distance.__members__.items():
            if m == value.upper():
                return mm


def get_distances_as_json():
    all_distances = []
    for distance in Distance:
        all_distances.append('{"value" : "' + distance.name + '", "text" : "' + distance.value + '"}')

    as_json_list = '[' + ','.join(all_distances) + ']'
    return as_json_list
