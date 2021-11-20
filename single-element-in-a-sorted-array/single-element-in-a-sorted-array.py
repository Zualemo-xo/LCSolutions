class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        for j in d:
            if(d[j]==1):
                return(j)
        