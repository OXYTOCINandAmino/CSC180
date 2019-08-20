class ttt:

 T=[0,0,0,0,0,0,0,0,0]
 
#printBoard
 def printBoard(self):
     L=[0,1,2,3,4,5,6,7,8]    
     for i in range(0,9):
         if(len(self.T)!=9)or((self.T[i]!=1)and(self.T[i]!=2)and(self.T[i]!=0)):
             return(False)
         else:
              if self.T[i]==0:
                 L[i]=i
              elif self.T[i]==1:
                 L[i]='X'
              elif self.T[i]==2:
                 L[i]='O'

     print (L[0],'|',L[1],'|',L[2])
     print ('---|---|---')
     print (L[3],'|',L[4],'|',L[5])
     print ('---|---|---') 
     print (L[6],'|',L[7],'|',L[8])
     return(True)


#analyzeBoard(self.T)
 def analyzeBoard(self):
     for i in range(0,9):
         if(len(self.T)!=9)or((self.T[i]!=1)and(self.T[i]!=2)and(self.T[i]!=0)):
             return(-1)
         else:
            if(self.T[0]==self.T[1]==self.T[2]==1)or(self.T[3]==self.T[4]==self.T[5]==1)or(self.T[6]==self.T[7]==self.T[8]==1)or(self.T[0]==self.T[3]==self.T[6]==1)or(self.T[1]==self.T[4]==self.T[7]==1)or(self.T[2]==self.T[5]==self.T[8]==1)or(self.T[0]==self.T[4]==self.T[8]==1)or(self.T[6]==self.T[4]==self.T[2]==1):
                return(1)
            if(self.T[0]==self.T[1]==self.T[2]==2)or(self.T[3]==self.T[4]==self.T[5]==2)or(self.T[6]==self.T[7]==self.T[8]==2)or(self.T[0]==self.T[3]==self.T[6]==2)or(self.T[1]==self.T[4]==self.T[7]==2)or(self.T[2]==self.T[5]==self.T[8]==2)or(self.T[0]==self.T[4]==self.T[8]==2)or(self.T[6]==self.T[4]==self.T[2]==2):
                return(2)
            else:
               if(self.T[0]!=0)and(self.T[1]!=0)and(self.T[2]!=0)and(self.T[3]!=0)and(self.T[4]!=0)and(self.T[5]!=0)and(self.T[6]!=0)and(self.T[7]!=0)and(self.T[8]!=0):
                   return(3)
               else:
                   return(0)



#Random Move
 def genRandomMove(self,player):
     for i in range(0,9):
          if(len(self.T)!=9)or((self.T[i]!=1)and(self.T[i]!=2)and(self.T[i]!=0)):
              return(-1)
     from random import randint
     Random_choose=randint(0,8)
     if(self.T[int(Random_choose)]!='1')and(self.T[int(Random_choose)]!='2'):
         return(Random_choose)
     else:
         return(-1)


#Wining Move
 def genWinningMove(self,player):
      for i in range(0,9):
           if(len(self.T)!=9)or((self.T[i]!=1)and(self.T[i]!=2)and(self.T[i]!=0)):
               return(-1)
      if((player!=1)and(player!=2)):
         return(-1)
      else:
	      if(player==1):
		      if((self.T[0]==self.T[1]==1)and(self.T[2]==0)):
			      return(2)
		      if((self.T[0]==self.T[2]==1)and(self.T[1]==0)):
			      return(1)
		      if((self.T[1]==self.T[2]==1)and(self.T[0]==0)):
			      return(0)
		      if((self.T[3]==self.T[4]==1)and(self.T[5]==0)):
			      return(5)
		      if((self.T[3]==self.T[5]==1)and(self.T[4]==0)):
			      return(4)
		      if((self.T[4]==self.T[5]==1)and(self.T[3]==0)):
			      return(3)
		      if((self.T[6]==self.T[7]==1)and(self.T[8]==0)):
			      return(8)
		      if((self.T[6]==self.T[8]==1)and(self.T[7]==0)):
			      return(7)
		      if((self.T[7]==self.T[8]==1)and(self.T[6]==0)):
			      return(6)
		      if((self.T[0]==self.T[3]==1)and(self.T[6]==0)):
			      return(6)
		      if((self.T[0]==self.T[6]==1)and(self.T[3]==0)):
			      return(3)
		      if((self.T[6]==self.T[3]==1)and(self.T[0]==0)):
			      return(0)
		      if((self.T[1]==self.T[4]==1)and(self.T[7]==0)):
			      return(7)
		      if((self.T[1]==self.T[7]==1)and(self.T[4]==0)):
			      return(4)
		      if((self.T[4]==self.T[7]==1)and(self.T[1]==0)):
			      return(1)
		      if((self.T[2]==self.T[5]==1)and(self.T[8]==0)):
			      return(8)
		      if((self.T[2]==self.T[8]==1)and(self.T[5]==0)):
			      return(5)
		      if((self.T[5]==self.T[8]==1)and(self.T[2]==0)):
			      return(2)
		      if((self.T[0]==self.T[4]==1)and(self.T[8]==0)):
			      return(8)
		      if((self.T[0]==self.T[8]==1)and(self.T[4]==0)):
			      return(4)
		      if((self.T[4]==self.T[8]==1)and(self.T[0]==0)):
			      return(0)
		      if((self.T[6]==self.T[4]==1)and(self.T[2]==0)):
			      return(2)
		      if((self.T[6]==self.T[2]==1)and(self.T[4]==0)):
			      return(4)
		      if((self.T[4]==self.T[2]==1)and(self.T[6]==0)):
			      return(6)
	      if(player==2):
		      if((self.T[0]==self.T[1]==2)and(self.T[2]==0)):
			      return(2)
		      if((self.T[0]==self.T[2]==2)and(self.T[1]==0)):
			      return(1)
		      if((self.T[1]==self.T[2]==2)and(self.T[0]==0)):
			      return(0)
		      if((self.T[3]==self.T[4]==2)and(self.T[5]==0)):
			      return(5)
		      if((self.T[3]==self.T[5]==2)and(self.T[4]==0)):
			      return(4)
		      if((self.T[4]==self.T[5]==2)and(self.T[3]==0)):
			      return(3)
		      if((self.T[6]==self.T[7]==2)and(self.T[8]==0)):
			      return(8)
		      if((self.T[6]==self.T[8]==2)and(self.T[7]==0)):
			      return(7)
		      if((self.T[7]==self.T[8]==2)and(self.T[6]==0)):
			      return(6)
		      if((self.T[0]==self.T[3]==2)and(self.T[6]==0)):
			      return(6)
		      if((self.T[0]==self.T[6]==2)and(self.T[3]==0)):
			      return(3)
		      if((self.T[6]==self.T[3]==2)and(self.T[0]==0)):
			      return(0)
		      if((self.T[1]==self.T[4]==2)and(self.T[7]==0)):
			      return(7)
		      if((self.T[1]==self.T[7]==2)and(self.T[4]==0)):
			      return(4)
		      if((self.T[4]==self.T[7]==2)and(self.T[1]==0)):
			      return(1)
		      if((self.T[2]==self.T[5]==2)and(self.T[8]==0)):
			      return(8)
		      if((self.T[2]==self.T[8]==2)and(self.T[5]==0)):
			      return(5)
		      if((self.T[5]==self.T[8]==2)and(self.T[2]==0)):
			      return(2)
		      if((self.T[0]==self.T[4]==2)and(self.T[8]==0)):
			      return(8)
		      if((self.T[0]==self.T[8]==2)and(self.T[4]==0)):
			      return(4)
		      if((self.T[4]==self.T[8]==2)and(self.T[0]==0)):
			      return(0)
		      if((self.T[6]==self.T[4]==2)and(self.T[2]==0)):
			      return(2)
		      if((self.T[6]==self.T[2]==2)and(self.T[4]==0)):
			      return(4)
		      if((self.T[4]==self.T[2]==2)and(self.T[6]==0)):
			      return(6)

#NonLoser Move
 def genNonLoser(self,player):
      for i in range(0,9):
           if(len(self.T)!=9)or((self.T[i]!=1)and(self.T[i]!=2)and(self.T[i]!=0)):
               return(-1)
      if((player!=1)and(player!=2)):
         return(-1)
      else:
	      if(player==2):
		      if((self.T[0]==self.T[1]==1)and(self.T[2]==0)):
			      return(2)
		      if((self.T[0]==self.T[2]==1)and(self.T[1]==0)):
			      return(1)
		      if((self.T[1]==self.T[2]==1)and(self.T[0]==0)):
			      return(0)
		      if((self.T[3]==self.T[4]==1)and(self.T[5]==0)):
			      return(5)
		      if((self.T[3]==self.T[5]==1)and(self.T[4]==0)):
			      return(4)
		      if((self.T[4]==self.T[5]==1)and(self.T[3]==0)):
			      return(3)
		      if((self.T[6]==self.T[7]==1)and(self.T[8]==0)):
			      return(8)
		      if((self.T[6]==self.T[8]==1)and(self.T[7]==0)):
			      return(7)
		      if((self.T[7]==self.T[8]==1)and(self.T[6]==0)):
			      return(6)
		      if((self.T[0]==self.T[3]==1)and(self.T[6]==0)):
			      return(6)
		      if((self.T[0]==self.T[6]==1)and(self.T[3]==0)):
			      return(3)
		      if((self.T[6]==self.T[3]==1)and(self.T[0]==0)):
			      return(0)
		      if((self.T[1]==self.T[4]==1)and(self.T[7]==0)):
			      return(7)
		      if((self.T[1]==self.T[7]==1)and(self.T[4]==0)):
			      return(4)
		      if((self.T[4]==self.T[7]==1)and(self.T[1]==0)):
			      return(1)
		      if((self.T[2]==self.T[5]==1)and(self.T[8]==0)):
			      return(8)
		      if((self.T[2]==self.T[8]==1)and(self.T[5]==0)):
			      return(5)
		      if((self.T[5]==self.T[8]==1)and(self.T[2]==0)):
			      return(2)
		      if((self.T[0]==self.T[4]==1)and(self.T[8]==0)):
			      return(8)
		      if((self.T[0]==self.T[8]==1)and(self.T[4]==0)):
			      return(4)
		      if((self.T[4]==self.T[8]==1)and(self.T[0]==0)):
			      return(0)
		      if((self.T[6]==self.T[4]==1)and(self.T[2]==0)):
			      return(2)
		      if((self.T[6]==self.T[2]==1)and(self.T[4]==0)):
			      return(4)
		      if((self.T[4]==self.T[2]==1)and(self.T[6]==0)):
			      return(6)
	      if(player==1):
		      if((self.T[0]==self.T[1]==2)and(self.T[2]==0)):
			      return(2)
		      if((self.T[0]==self.T[2]==2)and(self.T[1]==0)):
			      return(1)
		      if((self.T[1]==self.T[2]==2)and(self.T[0]==0)):
			      return(0)
		      if((self.T[3]==self.T[4]==2)and(self.T[5]==0)):
			      return(5)
		      if((self.T[3]==self.T[5]==2)and(self.T[4]==0)):
			      return(4)
		      if((self.T[4]==self.T[5]==2)and(self.T[3]==0)):
			      return(3)
		      if((self.T[6]==self.T[7]==2)and(self.T[8]==0)):
			      return(8)
		      if((self.T[6]==self.T[8]==2)and(self.T[7]==0)):
			      return(7)
		      if((self.T[7]==self.T[8]==2)and(self.T[6]==0)):
			      return(6)
		      if((self.T[0]==self.T[3]==2)and(self.T[6]==0)):
			      return(6)
		      if((self.T[0]==self.T[6]==2)and(self.T[3]==0)):
			      return(3)
		      if((self.T[6]==self.T[3]==2)and(self.T[0]==0)):
			      return(0)
		      if((self.T[1]==self.T[4]==2)and(self.T[7]==0)):
			      return(7)
		      if((self.T[1]==self.T[7]==2)and(self.T[4]==0)):
			      return(4)
		      if((self.T[4]==self.T[7]==2)and(self.T[1]==0)):
			      return(1)
		      if((self.T[2]==self.T[5]==2)and(self.T[8]==0)):
			      return(8)
		      if((self.T[2]==self.T[8]==2)and(self.T[5]==0)):
			      return(5)
		      if((self.T[5]==self.T[8]==2)and(self.T[2]==0)):
			      return(2)
		      if((self.T[0]==self.T[4]==2)and(self.T[8]==0)):
			      return(8)
		      if((self.T[0]==self.T[8]==2)and(self.T[4]==0)):
			      return(4)
		      if((self.T[4]==self.T[8]==2)and(self.T[0]==0)):
			      return(0)
		      if((self.T[6]==self.T[4]==2)and(self.T[2]==0)):
			      return(2)
		      if((self.T[6]==self.T[2]==2)and(self.T[4]==0)):
			      return(4)
		      if((self.T[4]==self.T[2]==2)and(self.T[6]==0)):
			      return(6)


#Move
 def Move(self,x,player):
     if(self.T[x]==0):
         self.T[x] = player
         return True
     else:
         return False
         

        
    
 
