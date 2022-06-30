class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mid=nums[len(nums)//2] #either of the mid number can be taken , as it will lead to the same answer
        ans=0
        for i in nums:
            ans+=abs(mid-i)
        return(ans)