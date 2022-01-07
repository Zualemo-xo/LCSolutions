import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        # Reservoir Sampling
        ans=-1
        scope=1
        for i in range(0,len(self.nums)):
            if(self.nums[i]==target):
                #print(random.random())
                #print(scope,1.0/scope)
                if(random.random()<(1.0/scope)): #use float 1.0 not int ffs DAMN
                    ans=i
                scope+=1
        return(ans)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)