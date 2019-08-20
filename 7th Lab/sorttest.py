def bubbleSort(A):
    n=len(A)
    for j in range(1,n):
        for i in range(1,n):
            if(A[i-1]>A[i]):
                A1=A[i-1]
                A2=A[i]
                A[i-1]=A2
                A[i]=A1

    if(n!=0):
        return(True,A)
    else:
        return(False,A)
            
