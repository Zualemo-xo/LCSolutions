class Solution:
    def knightDialer(self, n: int) -> int:
        #Phonepad size is 4X3
        #Recursion + Cache memoized
        phonepad=[[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]]
        v1=[-1,1]
        v2=[-2,2]
        def isvalid(x,y):
            if(x>=0 and y>=0 and x<len(phonepad) and y<len(phonepad[0]) and phonepad[x][y]!=-1):
                return(True)
            return(False)
        @cache
        def solve(r,c,countleft):
            #Base Condition
            if(countleft==0):
                return(1)

            #Recurse for all 8 possibilities
            ans=0
            for i in v1:
                for j in v2:
                    if(isvalid(r+i,c+j)):
                        ans=ans+solve(r+i,c+j,countleft-1)
                
            for i in v2:
                for j in v1:
                    if(isvalid(r+i,c+j)):
                        ans=ans+solve(r+i,c+j,countleft-1)
            return(ans % (10**9+7))
            
            
        fans=0
        for row in range(0,len(phonepad)):
            for col in range(0,len(phonepad[row])):
                if(phonepad[row][col]!=-1):
                    #print(phonepad[row][col])
                    fans+=solve(row,col,n-1)
                    fans=fans % (10**9+7)
                    #print("ANS:",fans)
        return(fans)