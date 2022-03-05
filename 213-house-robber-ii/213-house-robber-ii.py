class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #EDGE
        if(len(nums)==1):
            return(nums[0])
        #if the last house is not robbed
        dp={}
        def helper1(cur):
            if(cur==0):
                return(nums[cur])
            if(cur==1):
                return(max(nums[cur],nums[cur-1]))
            if(cur not in dp):
                dp[cur]=max(helper1(cur-2)+nums[cur],helper1(cur-1))
            return(dp[cur])
        #if the last house is robbed, exclude the first house
        dp2={}
        def helper2(cur):
            if(cur==0):
                return(0)
            if(cur==1):
                return(max(nums[cur],0))
            if(cur not in dp2):
                dp2[cur]=max(helper2(cur-2)+nums[cur],helper2(cur-1))
            return(dp2[cur])
        return(max(helper1(len(nums)-2),helper2(len(nums)-1)))