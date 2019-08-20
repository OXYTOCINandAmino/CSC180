3f=open('CSVFILE-IN','r')
lines=f.readlines()
f.close()
accum=[]

for i in lines:
   j=i.split('\n')[0]  
   k=j.split(',')      
   r=[]
   for x in k:
      r = r + [float(x)]
   accum = accum + [r]

col=int(raw_input('column'))
direction=raw_input('+/-')

   
def genSortKey(col,direction):
     def key(x):
         if(direction=='+'):
             return x[col]
         else:
             return -x[col]
     return key

L=sorted(accum,key=genSortKey(col,direction))

g=open('CSVFILE-OUT','w')

for line in L:
    g.write(str(line)+'\n')

    



