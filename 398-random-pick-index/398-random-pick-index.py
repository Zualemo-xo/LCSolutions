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
        l=[]
        ans=-1
        for i in range(0,len(self.nums)):
            if(self.nums[i]==target):
                l.append(i)
        x=random.randrange(0,len(l))
        return(l[x])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)