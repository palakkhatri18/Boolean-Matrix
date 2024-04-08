#Given a boolean matrix of size RxC where each cell contains either 0 or 1, modify it such that if a matrix cell matrix[i][j] is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(matrix):
    # code here 
    r = len(matrix)  
    c = len(matrix[0]) 

    R = [0] * r
    C = [0] * c

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1:
                R[i] = 1
                C[j] = 1
    
    for i in range(r):
        for j in range(c):
            matrix[i][j] = R[i] or C[j]
