def input_matrix(row, col):
    matrix = []
    for r in range(row):
        temp = list(map(int, input().split()))
        matrix.append(temp)
    return matrix


def print_matrix(matrix, row, col):
    for r in range(row):
        for c in range(col):
            print(str(matrix[r][c]).ljust(2), end=' ')
        print()


row, col = [int(i) for i in input().split()]
matrix = input_matrix(row, col)
print_matrix(matrix, row, col)