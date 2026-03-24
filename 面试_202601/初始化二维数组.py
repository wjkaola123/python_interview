rows = 3
cols = 4

matrix = [[0 for _ in range(cols)] for _ in range(rows)]

print(matrix)

for i in range(rows):
    if i % 2 == 0:
        for j in range(cols):
            matrix[i][j] = 2
    else:
        for j in range(cols):
            matrix[i][j] = 1

print(matrix)
