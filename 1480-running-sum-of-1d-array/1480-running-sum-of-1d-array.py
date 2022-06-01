class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #not prefixS 1liner
        return(sum(nums[0:i+1]) for i in range(0,len(nums)) )