class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #DFS WITH MEMOIZATION 
        self.maxn=float("-inf")
        @cache
        def helper(pos,val):
            if(pos==len(nums)):
                return
            
            val*=nums[pos]
            
            if(val>self.maxn):
                self.maxn=val
                
            if(val<=0):
                helper(pos+1,1)
            helper(pos+1,val)
        helper(0,1)
        return(self.maxn)