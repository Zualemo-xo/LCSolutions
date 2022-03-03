class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp=[0,0]
        for i in range(2,len(nums)):
            if(nums[i]-nums[i-1]==nums[i-1]-nums[i-2]):
                dp.append(dp[-1]+1) # dp stores eg 234 and 1234 --count is 2
            else:
                dp.append(0)
        return(sum(dp))