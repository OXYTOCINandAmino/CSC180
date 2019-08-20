def fibo(n):
    if(n<=0):
        return 1
    elif(n==1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)




def fiboL(n):
    X=[]
    for i in range(0,n+1):
        X=X+[fibo(i)]
    return X



def redfibo(n):
    def reducing_product(a,b):
        return a*b
    product=reduce(reducing_product,fiboL(n))
    return product

    
