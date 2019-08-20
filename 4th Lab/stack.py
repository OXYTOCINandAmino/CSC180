class stack:

    S=[]
    
    def push(self,x):
        self.S=self.S+[x]
        return self.S

    def pop(self):
        if(len(self.S)<=0):
            return False
        else:
            n=self.S[len(self.S)-1]
            self.S = list(self.S[0:len(self.S)-1])
            return n

    def disp(self):
        if(len(self.S)<0):
            return False
        
        else:
            for i in range(0,len(self.S)):
                print self.store[i],"<--top--" if i==0 else ""
                
        

    
