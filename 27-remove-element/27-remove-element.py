class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        while(True):
            if(len(nums)<=i):
                break
            print(nums)
            if(nums[i]==val):
                nums.pop(i)
                i+=0
            else:
                i+=1
        