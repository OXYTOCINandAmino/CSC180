class atom:
    def __init__(self,atomic_number):
        self.Atom_number = atomic_number
        self.bondList = []

    def addBond(self, arg1,arg2):
        self.bondList = self.bondList+[[arg1,arg2]]
        return self.bondList

    def genFormula(self):
        L=[]
        M=[]
        N=[]
        x=0
        y=0

        A=self.bondList+[[0,self.Atom_number]]
        for i in range(0,len(A)):
            L=L+[A[i][1]]

        for i in range(0,200):
            N=N+[0]

        for i in L:
            N[i]=N[i]+1

        for i in range(0,200):
            if(N[i]!=0):
                x=x+1

        for i in range(0,2*x):
            M=M+[0]

        for i in range(0,200):
            if(N[i]!=0):
                M[y]=i
                M[y+1]=N[i]
                y=y+2

        for i in range(0,len(M)):
            if(i==0):
                M[i]=str(M[i])
            else:
                M[i]='_'+str(M[i])

        string=""
        for i in M:
            string=string+i

        return string

            
            
        


    
