def ge_fw(matrix):
    n_row=len(matrix)
    n_col=len(matrix[0])
    M=[]
    for i in range(0,n_row):
        M=M+[[]]
    M[0]=matrix
    for i in range(0,n_row-1):
        FW(M[i])
        M[i+1]=FWsub_matrix(M[i])
        FWsubstitude_submatrix_into_original(matrix,M[i])
    return matrix

#
def FW(matrix):
    n_row=len(matrix)
    n_col=len(matrix[0])

    for a in range(0,n_row):
        if(matrix[a][0]!=0):
            M0=matrix[0]
            Ma=matrix[a]
            matrix[0]=Ma
            matrix[a]=M0
            break

    for b in range(0,n_row):
        if(matrix[b][0]!=0):
            A=matrix[b][0]
            for c in range(0,n_col):
                matrix[b][c]=float(matrix[b][c])/A

    for d in range(1,n_row):
        if(matrix[d][0]!=0):
            for e in range(0,n_col):
                matrix[d][e]=matrix[d][e]-matrix[0][e]
                
    return(matrix)

def FWsub_matrix(matrix):
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

def FWsubstitude_submatrix_into_original(matrix,L1):
    m_row=len(L1)
    m_col=len(L1[0])
    n_row=len(matrix)
    n_col=len(matrix[0])
    o=n_row-m_row
    p=n_col-m_col
    for i in range(0,m_row):
        for j in range(0,m_col):
            matrix[o+i][p+j]=L1[i][j]

    return matrix
#


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

    for d in range(0,n_row-1):
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


      
