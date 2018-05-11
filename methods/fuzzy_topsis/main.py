from fuzzy_sets.type1.triangle import TriangleType1FS


class FuzzyTOPSISType1FS:
    """
                           A1               A2
    data_matrix: C1 [x11, y11, z11]  [x21, y21, z21]
                 C2 [x12, y12, z12]  [x22, y22, z22]

                 [[FS1, FS2], [FS3, FS4]]
    """

    def __init__(self, criteria: list, alternatives: list, data_matrix, weights: list):
        self.criteria = criteria
        self.alternatives = alternatives
        self.data_matrix = data_matrix
        self.weights = weights

        self.normalized_matrix = None
        self.weighted_matrix = None

        self.fnis = None
        self.fpis = None

        self.distances = None
        self.scores = None

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

    def _get_maximum_right_boundary(self, matrix, index):
        """ Get maximum right boundary for a given criteria """
        vector = matrix[index]
        maximum_boundary = vector[0].z[0]  # works only for type 1 fs
        for fs in vector:
            if fs.z[0] > maximum_boundary:
                maximum_boundary = fs.z[0]
        return maximum_boundary

    def _get_minimum_left_boundary(self, matrix, index):
        """ Get maximum right boundary for a given criteria """
        vector = matrix[index]
        minimum_boundary = vector[0].x[0]  # works only for type 1 fs
        for fs in vector:
            if fs.x[0] < minimum_boundary:
                minimum_boundary = fs.x[0]
        return minimum_boundary

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

    def get_fnis(self):
        self.fnis = []
        for i, criterion in enumerate(self.weighted_matrix):
            maximum_right_boundary = self._get_maximum_right_boundary(self.weighted_matrix, i)
            self.fnis.append(
                TriangleType1FS(
                    (maximum_right_boundary, 1),
                    (maximum_right_boundary, 1),
                    (maximum_right_boundary, 1)
                )
            )

    def get_fpis(self):
        self.fpis = []
        for i, criterion in enumerate(self.weighted_matrix):
            minimum_left_boundary = self._get_minimum_left_boundary(self.weighted_matrix, i)
            self.fpis.append(
                TriangleType1FS(
                    (minimum_left_boundary, 1),
                    (minimum_left_boundary, 1),
                    (minimum_left_boundary, 1)
                )
            )

    def _transpose_matrix(self, matrix):
        transposed_matrix = []
        len_row = len(matrix[0])
        for i in range(len_row):
            new_row = []
            for criterion in matrix:
                new_row.append(criterion[i])
            transposed_matrix.append(new_row)
        return transposed_matrix

    def _get_distance_to_fpis(self, criteria_vector):
        distance = 0
        for i, ideal_positive in enumerate(self.fpis):
            distance += TriangleType1FS.distance(criteria_vector[i], ideal_positive)
        return distance

    def _get_distance_to_fnis(self, criteria_vector):
        distance = 0
        for i, ideal_negative in enumerate(self.fnis):
            distance += TriangleType1FS.distance(criteria_vector[i], ideal_negative)
        return distance

    def _get_closeness_coefficient(self, positive_distance, negative_distance):
        return negative_distance / (positive_distance + negative_distance)

    def get_alternatives_scores(self):
        self.scores = {}
        transposed_matrix = self._transpose_matrix(self.weighted_matrix)
        for i, alternative in enumerate(transposed_matrix):
            positive_distance = self._get_distance_to_fpis(alternative)
            negative_distance = self._get_distance_to_fnis(alternative)
            score = self._get_closeness_coefficient(positive_distance, negative_distance)
            self.scores[self.alternatives[i]] = score

    def perform(self):
        self.get_normalized_matrix()
        self.get_weighted_matrix()
        self.get_fnis()
        self.get_fpis()
        self.get_alternatives_scores()


def correctness_test():
    bad = TriangleType1FS((0, 0), (1, 1), (2, 0))
    normal = TriangleType1FS((1, 0), (2, 1), (3, 0))
    good = TriangleType1FS((2, 0), (3, 1), (4, 0))
    excelent = TriangleType1FS((3, 0), (4, 1), (5, 0))

    criteria = ['C1', 'C2', 'C3', 'C4']
    alternatives = ['A1', 'A2', 'A3', 'A4']
    data_matrix = [
        [bad, normal, good, excelent],
        [bad, normal, good, excelent],
        [bad, normal, good, excelent],
        [bad, normal, good, excelent],
    ]
    weights = [bad, normal, good, excelent]

    fuzzy_topsis = FuzzyTOPSISType1FS(criteria, alternatives, data_matrix, weights)
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

    fuzzy_topsis = FuzzyTOPSISType1FS(criteria, alternatives, data_matrix, weights)
    fuzzy_topsis.perform()
    print(fuzzy_topsis.scores)

if __name__ == '__main__':
    criteria = ['C1', 'C2']
    alternatives = ['A1', 'A2']
    data_matrix = [[TriangleType1FS((0, 0), (1, 1), (2, 0)), TriangleType1FS((1, 0), (2, 1), (3, 0))],
                   [TriangleType1FS((2, 0), (3, 1), (4, 0)), TriangleType1FS((3, 0), (4, 1), (5, 0))]]
    weights = [TriangleType1FS((0, 0), (1, 1), (2, 0)), TriangleType1FS((1, 0), (2, 1), (3, 0))]

    fuzzy_topsis = FuzzyTOPSISType1FS(criteria, alternatives, data_matrix, weights)
    fuzzy_topsis.get_normalized_matrix()
    print(fuzzy_topsis.normalized_matrix)

    fuzzy_topsis.get_weighted_matrix()
    print(fuzzy_topsis.weighted_matrix)

    fuzzy_topsis.get_fnis()
    print(fuzzy_topsis.fnis)

    fuzzy_topsis.get_fpis()
    print(fuzzy_topsis.fpis)

    fuzzy_topsis.get_alternatives_scores()
    print(fuzzy_topsis.scores)

    print('*' * 30)
    correctness_test()

    print('*' * 30)
    real_data_test()
