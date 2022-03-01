class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l=[]
        for i in range(0,n+1):
            x=bin(i)[2:]
            cnt=0
            for j in x:
                if(j=="1"):
                    cnt+=1
            l.append(cnt)
        return(l)
        