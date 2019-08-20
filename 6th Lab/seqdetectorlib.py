class seqdetector:
    def __init__(self):
        self.sequence=[]


    def evolve(self,word):
        if (word=="Cario"):
            self.sequence=["Cario"]
            print self.sequence
        else:
            self.sequence=self.sequence+[word]
            print self.sequence
            if(self.sequence==["Cario","is","really","handsome"]):
                return True
            else:
                return False
            

            
