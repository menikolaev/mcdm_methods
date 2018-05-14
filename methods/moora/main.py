from math import sqrt

from fuzzy_sets.type1.triangle import TriangleType1FS


class FuzzyMOORAType1FS:
    """
                           A1               A2
    data_matrix: C1 [x11, y11, z11]  [x21, y21, z21]
                 C2 [x12, y12, z12]  [x22, y22, z22]

                 [[FS1, FS2], [FS3, FS4]]
    """

    zero_fs = TriangleType1FS((0, 0), (0, 1), (0, 0))

    def __init__(self, criteria: list, alternatives: list, data_matrix, weights: list,
                 beneficial_attributes: list, non_beneficial_attributes: list):
        self.criteria = criteria
        self.alternatives = alternatives
        self.data_matrix = data_matrix
        self.weights = weights

        self.normalized_matrix = None
        self.weighted_matrix = None

        self.beneficial_attributes = beneficial_attributes
        self.non_beneficial_attributes = non_beneficial_attributes

        self.scores = None

    def _get_maximum_right_boundary(self, matrix, index):
        """ Get maximum right boundary for a given criteria """
        vector = matrix[index]
        maximum_boundary = vector[0].z[0]  # works only for type 1 fs
        for fs in vector:
            if fs.z[0] > maximum_boundary:
                maximum_boundary = fs.z[0]
        return maximum_boundary

    def get_normalized_matrix(self):
        self.normalized_matrix = []
        for i, criterion in enumerate(self.data_matrix):
            max_boundary = self._get_maximum_right_boundary(self.data_matrix, i)
            normalized_criterion = []
            for fs in criterion:
                normalized_criterion.append(
                    TriangleType1FS(
                        (round(fs.x[0] / max_boundary, 3), fs.x[1]),
                        (round(fs.y[0] / max_boundary, 3), fs.y[1]),
                        (round(fs.z[0] / max_boundary, 3), fs.z[1])
                    )
                )
            self.normalized_matrix.append(normalized_criterion)

    def get_weighted_matrix(self):
        if self.normalized_matrix is None:
            raise ValueError('Get normalized matrix first of all')

        self.weighted_matrix = []
        for i, criterion in enumerate(self.normalized_matrix):
            weight = self.weights[i]
            weighted_criterion = []
            for fs in criterion:
                weighted_criterion.append(fs * weight)
            self.weighted_matrix.append(weighted_criterion)

    def get_beneficial_fuzzy_set(self, criteria_vector):
        result = self.zero_fs
        for i, criterion in enumerate(criteria_vector):
            criterion_name = self.criteria[i]
            if criterion_name in self.beneficial_attributes:
                if not result:
                    result = criterion
                else:
                    result += criterion
        return result

    def get_non_beneficial_fuzzy_set(self, criteria_vector):
        result = self.zero_fs
        for i, criterion in enumerate(criteria_vector):
            criterion_name = self.criteria[i]
            if criterion_name in self.non_beneficial_attributes:
                if not result:
                    result = criterion
                else:
                    result += criterion
        return result

    def get_normalized_assessment_value(self, criteria_vector):
        beneficial_fs = self.get_beneficial_fuzzy_set(criteria_vector)
        non_beneficial_fs = self.get_non_beneficial_fuzzy_set(criteria_vector)

        squares_sub = beneficial_fs.square_sub(non_beneficial_fs)
        score = sqrt(1 / 3 * squares_sub)

        return score

    def _transpose_matrix(self, matrix):
        transposed_matrix = []
        len_row = len(matrix[0])
        for i in range(len_row):
            new_row = []
            for criterion in matrix:
                new_row.append(criterion[i])
            transposed_matrix.append(new_row)
        return transposed_matrix

    def get_alternatives_scores(self):
        self.scores = {}
        transposed_matrix = self._transpose_matrix(self.weighted_matrix)
        for i, alternative in enumerate(transposed_matrix):
            normalazed_assesment_value = self.get_normalized_assessment_value(alternative)
            self.scores[self.alternatives[i]] = normalazed_assesment_value

    def perform(self):
        self.get_normalized_matrix()
        self.get_weighted_matrix()
        self.get_alternatives_scores()


def correctness_test():
    bad = TriangleType1FS((0, 0), (1, 1), (2, 0))
    normal = TriangleType1FS((1, 0), (2, 1), (3, 0))
    good = TriangleType1FS((2, 0), (3, 1), (4, 0))
    excelent = TriangleType1FS((3, 0), (4, 1), (5, 0))

    criteria = ['C1', 'C2', 'C3', 'C4']
    beneficial = ['C1', 'C2']
    non_beneficial = ['C3', 'C4']
    alternatives = ['A1', 'A2', 'A3', 'A4']
    data_matrix = [
        [bad, normal, good, excelent],
        [bad, normal, good, excelent],
        [bad, normal, good, excelent],
        [bad, normal, good, excelent],
    ]
    weights = [bad, normal, good, excelent]

    fuzzy_topsis = FuzzyMOORAType1FS(criteria, alternatives, data_matrix, weights, beneficial, non_beneficial)
    fuzzy_topsis.perform()
    print(fuzzy_topsis.scores)


def real_data_test():
    VB = LI = TriangleType1FS((0, 0), (1, 1), (2, 0))
    B = I = TriangleType1FS((1, 0), (2, 1), (3, 0))
    N = MI = TriangleType1FS((2, 0), (3, 1), (4, 0))
    G = VI = TriangleType1FS((3, 0), (4, 1), (5, 0))
    E = EI = TriangleType1FS((4, 0), (5, 1), (6, 0))

    criteria = [
        'Performance', 'Web filtering (UTM)', 'Antivirus (UTM)', 'Intrusion prevention/detection (UTM)', 'Management',
        'Networking', 'Completeness (Functionality)', 'Correctness (Functionality)', 'Security', 'Efficiency',
        'Maintainability', 'Vendor Capabilities (Strategic)', 'Business Issues (Strategic)', 'Cost (Strategic)'
    ]
    beneficial = ['Performance', 'Web filtering (UTM)', 'Antivirus (UTM)', 'Intrusion prevention/detection (UTM)',
                  'Management', 'Networking', 'Completeness (Functionality)', 'Correctness (Functionality)']
    non_beneficial = ['Security', 'Efficiency', 'Maintainability', 'Vendor Capabilities (Strategic)',
                      'Business Issues (Strategic)', 'Cost (Strategic)']
    alternatives = ['Cisco ASAv', 'Juniper vSRX', 'Fortigate VMX NGFW', 'Palo Alto VM-Series']
    data_matrix = [
        [G, G, G, E],
        [N, G, E, N],
        [N, N, G, E],
        [N, G, G, G],
        [B, N, E, B],
        [G, G, G, G],
        [E, G, E, N],
        [N, N, G, G],
        [G, N, E, E],
        [N, G, G, N],
        [G, N, G, N],
        [N, N, G, G],
        [N, B, N, N],
        [B, N, VB, B]
    ]
    weights = [I, MI, MI, VI, LI, MI, I, I, VI, MI, LI, EI, VI, VI]

    fuzzy_topsis = FuzzyMOORAType1FS(criteria, alternatives, data_matrix, weights, beneficial, non_beneficial)
    fuzzy_topsis.perform()
    print(fuzzy_topsis.scores)


if __name__ == '__main__':
    criteria = ['C1', 'C2']
    beneficial = ['C1']
    non_beneficial = ['C2']
    alternatives = ['A1', 'A2']
    data_matrix = [[TriangleType1FS((0, 0), (1, 1), (2, 0)), TriangleType1FS((1, 0), (2, 1), (3, 0))],
                   [TriangleType1FS((2, 0), (3, 1), (4, 0)), TriangleType1FS((3, 0), (4, 1), (5, 0))]]
    weights = [TriangleType1FS((0, 0), (1, 1), (2, 0)), TriangleType1FS((1, 0), (2, 1), (3, 0))]

    fuzzy_moora = FuzzyMOORAType1FS(criteria, alternatives, data_matrix, weights, beneficial, non_beneficial)
    fuzzy_moora.get_normalized_matrix()
    print(fuzzy_moora.normalized_matrix)

    fuzzy_moora.get_weighted_matrix()
    print(fuzzy_moora.weighted_matrix)

    fuzzy_moora.get_alternatives_scores()
    print(fuzzy_moora.scores)

    print('*' * 30)
    correctness_test()

    print('*' * 30)
    real_data_test()
