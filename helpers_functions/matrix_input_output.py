def input_matrix(row_col):
    matrix = []
    for r in range(row_col[0]):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


def print_matrix(matrix, row_col, space=2):
    for r in range(row_col[0]):
        for c in range(row_col[1]):
            print(str(matrix[r][c]).ljust(space), end=' ')
        print()


row_col = list(map(int, input().split()))
matrix = input_matrix(row_col)
print_matrix(matrix, row_col)
