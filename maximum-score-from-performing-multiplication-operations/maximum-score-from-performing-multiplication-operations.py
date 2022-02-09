class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache(2000)
        def helper(i,l):
            if(i==m):
                return(0)
            r=n-1-(i-l)
            return(max(multipliers[i]*nums[l]+helper(i+1,l+1),  multipliers[i]*nums[r]+helper(i+1,l)))
        n,m=len(nums),len(multipliers)
        x=helper(0,0)
        helper.cache_clear()
        return(x)