class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        cnt=0
        for i in range(0,len(nums)):
            if(nums[i]==target):
                cnt+=1
                return(i)
            elif(nums[i]>target):
                cnt+=1
                return(i)
        if(cnt==0):
            return(len(nums))