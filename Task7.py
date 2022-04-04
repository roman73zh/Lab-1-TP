def transpose(mat):
    tmp = [list(row) for row in zip(*mat)]
    mat.clear()
    for i in tmp:
        mat.append(i)


matrix = [[1, 2], [3, 4]]
transpose(matrix)
for line in matrix:
    print(*line)
