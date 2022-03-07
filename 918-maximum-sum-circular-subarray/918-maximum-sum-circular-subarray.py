class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #kadane's case 1 max subarray
        maxn,curr=float("-inf"),0
        for i in range(0,len(nums)):
            curr+=nums[i]
            if(curr>maxn):
                maxn=curr   
            if(curr<0):
                curr=0
        #case2 circular find min subarray with kadane's
        minn,curr=float("inf"),0
        totsum=0
        for i in range(0,len(nums)):
            totsum+=nums[i]
            curr+=nums[i]
            if(curr<minn):
                minn=curr   
            if(curr>0):
                curr=0
        maxn2=totsum-minn #to get max subarray if circular
        if(maxn2==0): #if array is fully -ve
            maxn2=float("-inf") 
        #print(maxn,maxn2)
        return(max(maxn,maxn2))