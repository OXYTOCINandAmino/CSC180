def fiboL(n):
    if(n==0):
        return [1]
    if(n==1):
        return [1,1]
    else:
        sumterm=fiboL(n-1)[n-1]+fiboL(n-1)[n-2]
        return fiboL(n-1)+[sumterm]

    
    
    
