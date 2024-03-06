def matrix(A,B):
    result=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(A[0])):
            row.append(A[i][j] * B[i][j])
        result.append(row)
    return result

A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]

addition_result = matrix(A, B)

# Print the result
for row in addition_result:
    print(row)