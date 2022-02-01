class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxval=0
        diff=0
        for i in range(1,len(prices)):
            diff+=prices[i]-prices[i-1]
            if(diff<0):
                diff=0
            else:
                maxval=max(maxval,diff)
        return(maxval)
        # besttimetobuy=prices[0]
        # profit=0
        # for i in range(1,len(prices)):
        #     if(prices[i]<besttimetobuy):
        #         besttimetobuy=prices[i]
        #     if(prices[i]-besttimetobuy>profit):
        #         profit=prices[i]-besttimetobuy
        # return(profit)
        