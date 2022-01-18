class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if(n==0):
            return(True)
        if(len(flowerbed)==1 and flowerbed[0]==0 and n==1):
            return(True)
        elif(len(flowerbed)==1):
            return(False)
        elif(len(flowerbed)==2 and sum(flowerbed)==0 and n==1):
            return(True)
        elif(len(flowerbed)==2):
            return(False)
        if(flowerbed[0]==0 and flowerbed[1]==0):
            flowerbed[0]=1
            n-=1
        if(flowerbed[len(flowerbed)-1]==0 and flowerbed[len(flowerbed)-2]==0):
            flowerbed[len(flowerbed)-1]=1
            n-=1
        for i in range(1,len(flowerbed)-1):
            if(flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0):
                n-=1
                flowerbed[i]=1
        if(n<=0):
            return(True)
        return(False)
            
            