from fuzzy_sets.type2.type2_fuzzy_set import Type2FuzzySet


class TriangleType2FS(Type2FuzzySet):
    def __init__(self, x1, x2, y, z1, z2):
        self.points = (x1, x2, y, z1, z2)

    def __add__(self, other):
        if isinstance(other, TriangleType2FS):
            return TriangleType2FS((round(self.points[0][0] + other.points[0][0], 3), self.points[0][1]),
                                   (round(self.points[1][0] + other.points[1][0], 3), self.points[1][1]),
                                   (round(self.points[2][0] + other.points[2][0], 3), self.points[2][1]),
                                   (round(self.points[3][0] + other.points[3][0], 3), self.points[3][1]),
                                   (round(self.points[4][0] + other.points[4][0], 3), self.points[4][1])
                                   )
        raise ValueError('No possibility to add non-type2 triangular FS')

    def __mul__(self, other):
        if isinstance(other, TriangleType2FS):
            return TriangleType2FS((round(self.points[0][0] * other.points[0][0], 3), self.points[0][1]),
                                   (round(self.points[1][0] * other.points[1][0], 3), self.points[1][1]),
                                   (round(self.points[2][0] * other.points[2][0], 3), self.points[2][1]),
                                   (round(self.points[3][0] * other.points[3][0], 3), self.points[3][1]),
                                   (round(self.points[4][0] * other.points[4][0], 3), self.points[4][1])
                                   )
        elif isinstance(other, (int, float)):
            return TriangleType2FS((round(self.points[0][0] * other, 3), self.points[0][1]),
                                   (round(self.points[1][0] * other, 3), self.points[1][1]),
                                   (round(self.points[2][0] * other, 3), self.points[2][1]),
                                   (round(self.points[3][0] * other, 3), self.points[3][1]),
                                   (round(self.points[4][0] * other, 3), self.points[4][1])
                                   )
        raise ValueError('No possibility to multiply')

    def __truediv__(self, other):
        if isinstance(other, TriangleType2FS):
            return TriangleType2FS((round(self.points[0][0] / other.points[4][0], 3), self.points[0][1]),
                                   (round(self.points[1][0] / other.points[3][0], 3), self.points[1][1]),
                                   (round(self.points[2][0] / other.points[2][0], 3), self.points[2][1]),
                                   (round(self.points[3][0] / other.points[1][0], 3), self.points[3][1]),
                                   (round(self.points[4][0] / other.points[0][0], 3), self.points[4][1])
                                   )
        raise ValueError('No possibility to divide')

    def __getattr__(self, item):
        if item == 'x1':
            return self.points[0]
        elif item == 'x2':
            return self.points[1]
        elif item == 'y':
            return self.points[2]
        elif item == 'z1':
            return self.points[3]
        elif item == 'z2':
            return self.points[4]

    def __str__(self):
        return '<Type2FS Triangle ({}, {}, {}, {}, {})>'.format(*self.points)

    def __repr__(self):
        return '<Type2FS Triangle ({}, {}, {}, {}, {})>'.format(*self.points)


ones_fuzzy_set = TriangleType2FS((1, 1), (1, 1), (1, 1), (1, 1), (1, 1))

if __name__ == '__main__':
    t1 = TriangleType2FS((1, 0), (1.5, 0), (2, 1), (2.5, 0), (3, 0))
    t2 = TriangleType2FS((2, 0), (2.5, 0), (3, 1), (3.5, 0), (4, 0))
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
