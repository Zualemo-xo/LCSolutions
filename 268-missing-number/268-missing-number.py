class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #TC:O(N) SC: O(1)
        S=sum(nums)
        actualS=(len(nums)*(len(nums)+1))//2
        return(actualS-S)
