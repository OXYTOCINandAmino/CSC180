class stack:
    Q=[]
    def pushQ(self,x):
        self.Q=self.Q+[x]
        return self.Q

    def popQ(self):
        if(len(self.Q)<=0):
            return(False)
        else:
            
            m=self.Q[0]
            self.Q = list(self.Q[1:len(self.Q)])
            return m
