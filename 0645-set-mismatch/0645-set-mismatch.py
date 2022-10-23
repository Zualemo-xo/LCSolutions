class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d=defaultdict(int)
        sumz=0
        n=len(nums)
        n=( n*(n+1) )//2
        for i in range(0,len(nums)):
            d[nums[i]]+=1
            if(d[nums[i]]>1):
                repeated=nums[i]
            sumz+=nums[i]
        missing=n-sumz+repeated 
        return([repeated,missing])