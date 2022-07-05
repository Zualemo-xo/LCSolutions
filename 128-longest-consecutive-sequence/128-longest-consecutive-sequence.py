class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return(0)
        
        nums=[float("-inf")]+nums+[float("inf")]
        ans,temp=0,0
        #print(hashtable)
        nums.sort()
        for i in range(1,len(nums)):
            if(nums[i]-nums[i-1]==0):
                continue
            elif(nums[i]-nums[i-1]!=1):
                ans=max(ans,temp)
                temp=0
            else:
                temp+=1
        return(ans+1)