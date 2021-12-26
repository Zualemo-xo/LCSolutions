class Solution:
    def kClosest(self, P, k):
        heap, euclidean = [], lambda x, y : x*x + y*y
        for i, (x, y) in enumerate(P):
            d = euclidean(x, y)
            if len(heap) == k:
                heappushpop(heap, (-d, i))     # -d to convert to max-heap (default is min)
            else: 
                heappush(heap, (-d, i))
        return [P[i] for (_, i) in heap]
        