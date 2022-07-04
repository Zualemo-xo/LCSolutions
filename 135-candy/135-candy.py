class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        ratings=[float("-inf")]+ratings+[float("-inf")] #to consider edge cases
        LefttoRight=[0]
        RighttoLeft=[0]
        cnt=0
        
        #Try left toright
        for i in range(1,len(ratings)-1):
            if(ratings[i]>ratings[i-1]):
                LefttoRight.append(LefttoRight[-1]+1)
            else:
                LefttoRight.append(1)
        #right to left
        for i in range(len(ratings)-2,0,-1):
            if(ratings[i]>ratings[i+1]):
                RighttoLeft.append(RighttoLeft[-1]+1)
            else:
                RighttoLeft.append(1)
        
        #remove 0's added as dummy variables        
        LefttoRight=LefttoRight[1:]
        RighttoLeft=RighttoLeft[1:]
        RighttoLeft.reverse()
        
        #print(LefttoRight,RighttoLeft)
        ans=0
        for i in range(0,len(LefttoRight)):
            ans+=max(LefttoRight[i],RighttoLeft[i])
        return(ans)