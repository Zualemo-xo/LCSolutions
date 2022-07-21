class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #bottom up dp
        dp=[0]*(max(nums)+1)
        #nums.sort()
        totnums=defaultdict(int)
        for i in nums:
            totnums[i]+=i
        #base case
        dp[0]=totnums[0]
        dp[1]=totnums[1]
        #i refers to no we gonna select, not index
        # we iterate from case of selecting number '0' till max number in given array
        for i in range(2,max(nums)+1):
            dp[i]=max(dp[i-1],dp[i-2]+totnums[i]) #either select this no and combine with i-2 or select i-1 and not consider current no 'i'.
        #print(dp)
        #print(totnums)
        return(dp[i])