class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        s=0
        for i in nums:
            if(i%2==0):
                s+=i
        ans=[]
        for q in queries:
            #print(nums)
            old=nums[q[1]]
            if(nums[q[1]]%2==0):
                s-=nums[q[1]]
            if(abs(old+q[0])%2==0):
                s+=old+q[0]
            nums[q[1]]=old+q[0]
            ans.append(s)
        return(ans)
            