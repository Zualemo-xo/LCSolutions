class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        besttimetobuy=[prices[0]]*len(prices)
        #besttimetobuy[0]=prices[0]
        
        for i in range(1,len(prices)):
            if(prices[i]<besttimetobuy[i-1]):
                besttimetobuy[i]=prices[i]
            else:
                besttimetobuy[i]=besttimetobuy[i-1]
        #print(besttimetobuy)
        
        profit=[0]*len(prices)
        for i in range(1,len(prices)):
            if(prices[i]-besttimetobuy[i]>profit[i-1]):
                profit[i]=prices[i]-besttimetobuy[i]
            else:
                profit[i]=profit[i-1]
        return(profit[len(profit)-1])
        