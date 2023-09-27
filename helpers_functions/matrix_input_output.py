def input_matrix(row):
    return [[int(i) for i in input().split()] for _ in range(row)]


def print_matrix(matrix, row):
    [print(matrix[i]) for i in range(row)]


row, col = [int(i) for i in input().split()]
matrix = input_matrix(row)
print_matrix(matrix, row)