class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        #Sort by dec order of units, select till truck space is exhausted
        #TC: O(NlogN) SC:(1)
        boxTypes.sort(key=lambda x:-x[1])
        ans=0
        for quantity,units in boxTypes:
            if(truckSize-quantity<0):
                needed=quantity+(truckSize-quantity)
                ans+=units*needed
                break
            else:
                truckSize-=quantity
                ans+=units*quantity
        return(ans)