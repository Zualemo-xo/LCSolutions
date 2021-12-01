class Solution:
    def rob(self, nums: List[int]) -> int:
        #memoization with cache
        #dp=[0]*len(nums)
        sumz=0
        self.maxsumz=0
        @cache
        def helper(pos,sumz):
            
            if(pos>=len(nums)):
                if(sumz>self.maxsumz):
                    self.maxsumz=sumz
                return()
            # if(dp[pos]!=0):
            #     return(dp[pos])
            #for i in range(0,len(nums)):
            sumz+=nums[pos]
            #print(dp)
            #dp[pos+1]=
            helper(pos+1,sumz-nums[pos])
            #dp[pos+2]=
            helper(pos+2,sumz)
        helper(0,0)
        #print(dp[pos])
        return(self.maxsumz)