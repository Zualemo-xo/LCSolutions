class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans=[]
        if(n%2!=0):
            n-=1
            ans.append(0)
        for i in range(0,n/2):
            ans.append(i+1)
            ans.append(-(i+1))
        return(ans)