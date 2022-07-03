class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        diff=[]
        #TC: O(2N)
        if(len(nums)<=2): #Edge c
            if(len(nums)==2 and nums[0]==nums[1]):
                return(1)
            return(len(nums))
        for i in range(1,len(nums)):
            diff.append(nums[i]-nums[i-1])
        #print(diff)
        isPositive=None
        cnt=0
        
        for i in range(0,len(diff)):
            if(isPositive==None and diff[i]!=0): #Initialize 
                isPositive=True if diff[i]>0 else False
                cnt+=1
                
            elif(isPositive and diff[i]<0):
                cnt+=1
                isPositive=False
            elif(isPositive==False and diff[i]>0):
                cnt+=1
                isPositive=True

        return(cnt+1)
        
        