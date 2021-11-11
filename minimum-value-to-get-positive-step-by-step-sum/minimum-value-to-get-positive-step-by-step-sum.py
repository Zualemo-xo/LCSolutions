class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minz=float("inf")
        t=0
        for i in nums:
            t+=i
            if(t<minz):
                minz=t
        return(abs(minz)+1 if minz<0 else 1)
            
        