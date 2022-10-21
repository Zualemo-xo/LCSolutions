class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d=defaultdict(list)
        for i in range(0,len(nums)):
            d[nums[i]].append(i)
        
        for i in d:
            for j in range(1,len(d[i])):
                if(abs(d[i][j-1]-d[i][j])<=k):
                    return(True)
        return(False)
                