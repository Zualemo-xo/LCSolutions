class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        #TC : O(N) SC:O(1)
        dp=0
        sumz=0
        for i in range(2,len(nums)):
            if(nums[i]-nums[i-1]==nums[i-1]-nums[i-2]):
                dp+=1 # dp stores eg 234 and 1234 --count is 2
                sumz+=dp
            else:
                dp=0
        return(sumz)