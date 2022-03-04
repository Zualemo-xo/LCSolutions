
class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxreach=0
        for i in range(0,len(nums)):
            if(i>maxreach):
                return(False)
            elif(i+nums[i]>maxreach):
                maxreach=i+nums[i]
            if(maxreach>=len(nums)-1):
                return(True)
        