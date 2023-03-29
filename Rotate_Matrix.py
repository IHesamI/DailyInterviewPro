def rotate(mat):
    n = len(mat)
    rotated_mat = []
    for each_row in range(len(mat)):
        new_row = []
        for each_column in range(n-1, -1, -1):
            new_row.append(mat[each_column][each_row])
        rotated_mat.append(new_row)
    return rotated_mat


mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
print(rotate(mat))
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
