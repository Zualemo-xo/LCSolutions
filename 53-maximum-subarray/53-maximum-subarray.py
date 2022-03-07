class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #kadane's
        #i found out the zsubarray which gives out max sum too lol
        gstart,end,start=0,0,0
        maxn,curr=float("-inf"),0
        for i in range(0,len(nums)):
            curr+=nums[i]
            if(curr>maxn):
                gstart=start
                end=i
                maxn=curr   
            if(curr<0):
                start=i+1
                curr=0
            
        return(maxn)