from fuzzy_sets.type1.type1_fuzzy_set import Type1FuzzySet


class TriangleType1FS(Type1FuzzySet):
    def __init__(self, x, y, z):
        self.points = (x, y, z)

    def __add__(self, other):
        if isinstance(other, TriangleType1FS):
            return TriangleType1FS((round(self.points[0][0] + other.points[0][0], 3), self.points[0][1]),
                                   (round(self.points[1][0] + other.points[1][0], 3), self.points[1][1]),
                                   (round(self.points[2][0] + other.points[2][0], 3), self.points[2][1])
                                   )
        raise ValueError('No possibility to add non-type2 triangular FS')

    def __mul__(self, other):
        if isinstance(other, TriangleType1FS):
            return TriangleType1FS((round(self.points[0][0] * other.points[0][0], 3), self.points[0][1]),
                                   (round(self.points[1][0] * other.points[1][0], 3), self.points[1][1]),
                                   (round(self.points[2][0] * other.points[2][0], 3), self.points[2][1])
                                   )
        elif isinstance(other, (int, float)):
            return TriangleType1FS((round(self.points[0][0] * other, 3), self.points[0][1]),
                                   (round(self.points[1][0] * other, 3), self.points[1][1]),
                                   (round(self.points[2][0] * other, 3), self.points[2][1])
                                   )
        raise ValueError('No possibility to multiply')

    def __truediv__(self, other):
        if isinstance(other, TriangleType1FS):
            return TriangleType1FS((round(self.points[0][0] / other.points[2][0], 3), self.points[0][1]),
                                   (round(self.points[1][0] / other.points[1][0], 3), self.points[1][1]),
                                   (round(self.points[2][0] / other.points[0][0], 3), self.points[2][1])
                                   )
        raise ValueError('No possibility to divide')

    def __getattr__(self, item):
        if item == 'x':
            return self.points[0]
        elif item == 'y':
            return self.points[1]
        elif item == 'z':
            return self.points[2]

    def __str__(self):
        return '<Type1FS Triangle ({}, {}, {})>'.format(*self.points)

    def __repr__(self):
        return '<Type1FS Triangle ({}, {}, {})>'.format(*self.points)

ones_fuzzy_set = TriangleType1FS((1, 1), (1, 1), (1, 1))

if __name__ == '__main__':
    t1 = TriangleType1FS((1, 0), (2, 1), (3, 0))
    t2 = TriangleType1FS((2, 0), (3, 1), (4, 0))
    t3 = t1 + t2
    print(t3)

    t4 = t1 * t2
    print(t4)

    t5 = t1 * 5
    print(t5)

    t6 = t1 * 3.5
    print(t6)

    t7 = ones_fuzzy_set/t1
    print(t7)
