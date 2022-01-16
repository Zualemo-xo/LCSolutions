class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dist=-1
        sit,prev=0,0
        for i in range(0,len(seats)):
            if( (i-prev>sit and seats[i]==0 and i+1==len(seats) )or (prev==0 and seats[0]==0 and seats[i]==1)):
                #print("ff",i)
                sit=i-prev
                dist=i-prev
                prev=i
            elif(i-prev>dist and seats[i]==1 ):
                #print(prev,i)
                sit=max(sit,max(1,(i-prev)//2) )
                dist=i-prev
                prev=i
                #print("wtf")
            if(seats[i]==1):
                prev=i
            #print("SIT:",sit) 
        #print("SITANS:",sit)
        return(sit)
                
                