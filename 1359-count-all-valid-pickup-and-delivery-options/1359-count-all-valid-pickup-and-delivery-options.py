class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        p=[1]
        for i in range(2,n+1):
            gaps=i*2-1 #possible places for insertion of new Pi,Di
            possibilities=(gaps*(gaps+1))/2 #athoda sum will give total ways we can place new Pi,Di
            p.append((possibilities*p[-1])%((10**9)+7))

        return(p[-1]%((10**9)+7))