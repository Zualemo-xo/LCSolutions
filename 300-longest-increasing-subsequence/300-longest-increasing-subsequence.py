class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[1 for i in range(0,len(nums))]
        cnt=0
        maxn=0
        for i in range(1,len(nums)):
            for j in range(0,i):
                if(nums[i]>nums[j]):
                    l[i]=max(l[i],l[j]+1)
        return(max(l))