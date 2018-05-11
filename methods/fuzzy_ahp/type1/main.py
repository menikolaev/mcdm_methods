import copy
from functools import reduce
from pprint import pprint

from fuzzy_sets.type1.triangle import TriangleType1FS
from methods.data import criteria_hierarchy, alternatives, data, criteria_data, high_level_criteria


class FuzzyAHPType1:
    """
    criteria_hierarchy:
            {
                'C1': 'C1',
                'C2': [
                        'C21',
                        'C22',
                      ],
                'C3': 'C3',
            }
    alternatives: list -> e.g. ['A1', 'A2', 'A3', 'A4']
    data (flat hierarchy):
            {
                'C1': matrix,
                'C2': matrix,
                'C3': matrix,
                ...
            }
    criteria_hierarchy:
            {
                'high_level': matrix, <- mandatory
                'subcriteria': {
                                  'high_level': matrix, <- mandatory if exists
                                  'subcriteria' ...
                               }
            }
    matrix = [
        [<row of variables>],
        [<row of variables>],
    ]
    """

    def __init__(self, criteria_hierarchy, alternatives, data, weights_hierarchy, mapping):
        self.mapping = mapping
        self.criteria_hierarchy = criteria_hierarchy
        self.alternatives = alternatives
        self.data = self.get_fuzzy_sets(data)
        self.weights_hierarchy = self.get_fuzzy_sets(weights_hierarchy)

    def get_fuzzy_sets(self, raw_data):
        new_data = copy.deepcopy(raw_data)

        def inner(data):
            if isinstance(data, dict):
                for key, value in data.items():
                    inner(value)
            elif isinstance(data, list):
                for i, item in enumerate(data):
                    if not isinstance(item, list):
                        if item in self.mapping:
                            data[i] = self.mapping[item]
                    else:
                        inner(item)
                return
            else:
                return

        inner(new_data)
        return new_data

    def _transpose_matrix(self, matrix):
        transposed_matrix = []
        len_row = len(matrix[0])
        for i in range(len_row):
            new_row = []
            for criterion in matrix:
                new_row.append(criterion[i])
            transposed_matrix.append(new_row)
        return transposed_matrix

    def _calculate_weights(self, matrix):
        tr_matrix = self._transpose_matrix(matrix)

        sums = []
        for item in tr_matrix:
            inner_sum = reduce(lambda x, y: x + y, item)
            sums.append(inner_sum)

        normalized_matrix = []
        for i, item in enumerate(tr_matrix):
            row = []
            for fs in item:
                row.append(fs * (self.mapping['one'] / sums[i]))
            normalized_matrix.append(row)

        tr_normalized_matrix = self._transpose_matrix(normalized_matrix)
        norm_sums = []
        for item in tr_normalized_matrix:
            inner_sum = reduce(lambda x, y: x + y, item)
            norm_sums.append(inner_sum)

        overall_sum = reduce(lambda x, y: x + y, norm_sums)
        return list(map(lambda x: x * (self.mapping['one'] / overall_sum), norm_sums))

    def calculate_weight_scores(self):
        scores = {}
        high_level = self.weights_hierarchy['high_level']
        high_level_scores = self._calculate_weights(high_level)

        for i, item in enumerate(high_level_scores):
            scores[high_level_criteria[i]] = item

        for key, value in self.weights_hierarchy['subcriteria'].items():
            subcriteria = value['high_level']
            subcr_scores = self._calculate_weights(subcriteria)
            criteria_index = high_level_criteria.index(key)
            high_level_score = high_level_scores[criteria_index]
            real_subscr_scores = list(map(lambda x: x * high_level_score, subcr_scores))

            for i, item in enumerate(real_subscr_scores):
                scores[self.criteria_hierarchy[key][i]] = item
        return scores

    def calculate_alternatives_matrix(self):
        matrix = []
        keys = []
        for key, value in self.data.items():
            vector = self._calculate_weights(value)
            matrix.append(vector)
            keys.append(key)

        tr_matrix = self._transpose_matrix(matrix)
        return tr_matrix, keys

    def defuzzification(self, fs):
        return (fs.x[0] + fs.y[0] + fs.z[0]) / 3

    def get_ranking(self):
        alternatives_matrix, criteria = self.calculate_alternatives_matrix()
        weight_scores = self.calculate_weight_scores()

        weight_vector = []
        for criterion in criteria:
            for key, value in weight_scores.items():
                if key == criterion:
                    weight_vector.append(value)

        final_scores = []
        for item in alternatives_matrix:
            score = reduce(lambda x, y: x + y, map(lambda x, y: x * y, item, weight_vector))
            non_fuzzy_score = self.defuzzification(score)
            final_scores.append(non_fuzzy_score)

        overall_score = sum(final_scores)
        normalized_scores = list(map(lambda x: x / overall_score, final_scores))
        return dict(zip(self.alternatives, normalized_scores))


if __name__ == '__main__':
    one = TriangleType1FS((1, 1), (1, 1), (1, 1))
    I1 = E1 = TriangleType1FS((1, 1), (1, 1), (2, 0))
    I2 = E2 = TriangleType1FS((1, 1), (2, 1), (3, 0))
    I3 = E3 = TriangleType1FS((2, 0), (3, 1), (4, 0))
    I4 = E4 = TriangleType1FS((3, 0), (4, 1), (5, 0))
    I5 = E5 = TriangleType1FS((4, 0), (5, 1), (6, 0))
    I6 = E6 = TriangleType1FS((5, 0), (6, 1), (7, 0))
    I7 = E7 = TriangleType1FS((6, 0), (7, 1), (8, 0))
    I8 = E8 = TriangleType1FS((7, 0), (8, 1), (9, 0))
    I9 = E9 = TriangleType1FS((8, 0), (9, 1), (9, 1))

    mapping = {
        'one': one,

        'I1': I1,
        'I2': I2,
        'I3': I3,
        'I4': I4,
        'I5': I5,
        'I6': I6,
        'I7': I7,
        'I8': I8,
        'I9': I9,

        'E1': E1,
        'E2': E2,
        'E3': E3,
        'E4': E4,
        'E5': E5,
        'E6': E6,
        'E7': E7,
        'E8': E8,
        'E9': E9,

        '1 / I1': one / I1,
        '1 / I2': one / I2,
        '1 / I3': one / I3,
        '1 / I4': one / I4,
        '1 / I5': one / I5,
        '1 / I6': one / I6,
        '1 / I7': one / I7,
        '1 / I8': one / I8,
        '1 / I9': one / I9,

        '1 / E1': one / E1,
        '1 / E2': one / E2,
        '1 / E3': one / E3,
        '1 / E4': one / E4,
        '1 / E5': one / E5,
        '1 / E6': one / E6,
        '1 / E7': one / E7,
        '1 / E8': one / E8,
        '1 / E9': one / E9,
    }

    fuzzy_ahp = FuzzyAHPType1(criteria_hierarchy, alternatives, data, criteria_data, mapping)
    pprint(fuzzy_ahp.data)
    pprint(fuzzy_ahp.weights_hierarchy)
    pprint(fuzzy_ahp.calculate_weight_scores())
    pprint(fuzzy_ahp.calculate_alternatives_matrix())
    pprint(fuzzy_ahp.get_ranking())
