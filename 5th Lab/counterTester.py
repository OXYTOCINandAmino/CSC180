class counter:
    
    def __init__(self,initCnt):
        self.cnt = initCnt

    def evolve(self,x):
        self.cnt=self.cnt+x

    def getState(self):
        return self.cnt

x=counter(1000)
y=counter(50)
z=counter(10)

x.evolve(100)
y.evolve(100)
z.evolve(100)

X=x.getState()
Y=y.getState()
Z=z.getState()

print X
print Y
print Z
