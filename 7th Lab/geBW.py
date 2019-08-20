def ge_bw(matrix):
    n_row=len(matrix)
    n_col=len(matrix[0])
    M=[]
    for i in range(0,n_row):
        M=M+[[]]
    M[0]=matrix
    for i in range(0,n_row-1):
        BW(M[i])
        M[i+1]=BWsub_matrix(M[i])
        BWsubstitude_submatrix_into_original(matrix,M[i])
    return matrix

#
def BW(matrix):
    n_row=len(matrix)
    n_col=len(matrix[0])

    if(n_row<n_col):
        n=n_row
    else:
        n=n_col

    for a in range(0,n_row):
        if(matrix[a][n-1]!=0):
            Mn=matrix[n_row-1]
            Ma=matrix[a]
            matrix[n_row-1]=Ma
            matrix[a]=Mn
            break

    for b in range(0,n_row):
        if(matrix[b][n-1]!=0):
            A=matrix[b][n-1]
        for c in range(0,n_col):
                matrix[b][c]=float(matrix[b][c])/A

    for d in range(0,n_row):
        if(matrix[d][n-1]!=0):
            for e in range(0,n_col):
                matrix[d][e]=matrix[d][e]-matrix[n_row-1][e]

                
    return(matrix)

def BWsub_matrix(matrix):
    n_row=len(matrix)
    n_col=len(matrix[0])
    L1=[]
    L2=[]
    for i in range(0,n_row-1):
        for j in range(0,n_col-1):
            L2=L2+[matrix[i][j]]
        L1=L1+[L2]
        L2=[]
    return(L1)

def BWsubstitude_submatrix_into_original(matrix,L1):
    m_row=len(L1)
    m_col=len(L1[0])
    n_row=len(matrix)
    n_col=len(matrix[0])
    for i in range(0,m_row):
        for j in range(0,m_col):
            matrix[i][j]=L1[i][j]

    return matrix

