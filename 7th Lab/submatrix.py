def sub_matrix(matrix):
    n_row=len(matrix)
    n_col=len(matrix[0])
    L1=[]
    L2=[]
    for i in range(1,n_row):
        for j in range(1,n_col):
            L2=L2+[matrix[i][j]]
        L1=L1+[L2]
        L2=[]


    return(L1)
    
        
