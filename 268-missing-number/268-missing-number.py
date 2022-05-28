class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=0
        nums.append(-1)
        nums.sort()
        for pos in range(1,len(nums)):
            if(nums[pos]-1!=nums[pos-1]):
                return(nums[pos]-1)
        return(len(nums)-1)
