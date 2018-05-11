import math


class FuzzySet:
    @staticmethod
    def distance(fs1, fs2):
        if len(fs1.points) != len(fs2.points):
            raise ValueError('Len of points in f1 and f2 are not equal')

        points_len = len(fs1.points)
        summary = 0
        for i in range(points_len):
            summary += (fs1.points[i][0] - fs2.points[i][0]) ** 2
        return math.sqrt(summary / points_len)


if __name__ == '__main__':
    fs1 = FuzzySet()
    fs1.points = ((0, 1), (0, 1), (0, 1))
    fs2 = FuzzySet()
    fs2.points = ((2, 1), (2, 1), (2, 1))

    print(FuzzySet.distance(fs1, fs2))
