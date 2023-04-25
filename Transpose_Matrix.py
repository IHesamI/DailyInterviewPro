def transpose(mat):
    # Fill this in.
    transposed_mat=[]
    column=0
    for row in mat:
        for i in range(len(row)):
            if column==0:
                transposed_mat.append([row[i]])
            else:
                transposed_mat[i].append(row[i])
        column+=1
    return transposed_mat
            
    
mat = [
    [1, 2, 3],
    [4, 5, 6],
]

print(transpose(mat))
# [[1, 4],
#  [2, 5], 
#  [3, 6]]