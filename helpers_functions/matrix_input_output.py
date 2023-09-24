def input_matrix(row, col):
    matrix = []
    for r in range(row):
        row = []
        for c in range(col):
            element = int(input())
            row.append(element)
        matrix.append(row)
    return matrix


def print_matrix(matrix, row, col, space=2):
    for r in range(row):
        for c in range(col):
            print(str(matrix[r][c]).ljust(space), end=' ')
        print()


row, col = int(input()), int(input())


matrix = input_matrix(row, col)
print_matrix(matrix, row, col)

