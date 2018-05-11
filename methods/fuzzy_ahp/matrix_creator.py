from itertools import zip_longest

input_line = ['1','4','1/5','2','1/4','1','1/7','1/3','5','7','1','3','1/2','3','1/3','1']

criteria_length = 4
mapping_type = 'equality'


def transpose_matrix(matrix):
    transposed_matrix = []
    len_row = len(matrix[0])
    for i in range(len_row):
        new_row = []
        for criterion in matrix:
            new_row.append(criterion[i])
        transposed_matrix.append(new_row)
    return transposed_matrix


mapping = {
    'equality': {
        '1': 'E1',
        '2': 'E2',
        '3': 'E3',
        '4': 'E4',
        '5': 'E5',
        '6': 'E6',
        '7': 'E7',
        '8': 'E8',
        '9': 'E9',
        '1/2': '1 / E2',
        '1/3': '1 / E3',
        '1/4': '1 / E4',
        '1/5': '1 / E5',
        '1/6': '1 / E6',
        '1/7': '1 / E7',
        '1/8': '1 / E8',
        '1/9': '1 / E9',
    },
    'importance': {
        '1': 'I1',
        '2': 'I2',
        '3': 'I3',
        '4': 'I4',
        '5': 'I5',
        '6': 'I6',
        '7': 'I7',
        '8': 'I8',
        '9': 'I9',
        '1/2': '1 / I2',
        '1/3': '1 / I3',
        '1/4': '1 / I4',
        '1/5': '1 / I5',
        '1/6': '1 / I6',
        '1/7': '1 / I7',
        '1/8': '1 / I8',
        '1/9': '1 / I9',
    }
}

fs_line = list(map(lambda x: mapping[mapping_type][x], input_line))


# print(fs_line)


def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return list(zip_longest(fillvalue=fillvalue, *args))


result = grouper(criteria_length, fs_line)

tr_result = transpose_matrix(result)

for item in tr_result:
    print(str(item) + ',')
