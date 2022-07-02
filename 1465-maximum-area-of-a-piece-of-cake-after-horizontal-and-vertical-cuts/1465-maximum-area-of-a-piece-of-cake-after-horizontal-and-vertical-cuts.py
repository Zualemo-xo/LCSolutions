class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        #TC: O(Nlog N) SC:O(1)
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()
        
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        hMaxDiff,vMaxDiff=0,0
        for i in range(1,len(horizontalCuts)):
            hMaxDiff=max(hMaxDiff, horizontalCuts[i]-horizontalCuts[i-1])
        
        for i in range(1,len(verticalCuts)):
            vMaxDiff=max(vMaxDiff, verticalCuts[i]-verticalCuts[i-1])
        return((hMaxDiff * vMaxDiff) % (10**9+7))
        