class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d=defaultdict(int)

        for i in nums:
            d[i]+=1
        ans=[]
        for j in range(1,len(nums)+1):
            if(j not in d):
                ans.append(j)
        return(ans)