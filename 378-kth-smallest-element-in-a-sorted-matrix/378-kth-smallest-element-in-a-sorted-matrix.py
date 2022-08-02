
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        #TC: O(N^3 log(N)) SC:O(N^2)
        l=[]
        for i in matrix:
            for j in i:
                heapq.heappush(l,j)
        while(k>0):
            k-=1
            ans=heapq.heappop(l)
        return(ans)
                