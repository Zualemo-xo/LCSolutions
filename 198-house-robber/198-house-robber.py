class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # top down dp
        mem={}
        def helper(i):
            #base cases
            if(i==0):
                return(nums[0])
            if(i==1):
                return(max(nums[0],nums[1]))
            #recurrence relation and memoization into dict 'mem'
            elif i not in mem:
                mem[i]=max(helper(i-1),helper(i-2)+nums[i])
            return(mem[i])
        
        return(helper(len(nums)-1))