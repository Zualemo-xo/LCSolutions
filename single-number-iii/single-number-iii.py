class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=defaultdict(int)
        for i in nums:
            l[i]+=1
        #print(l)
        ans=[]
        for key in l:
            if(l[key]==1):
                ans.append(key)
        return(ans)