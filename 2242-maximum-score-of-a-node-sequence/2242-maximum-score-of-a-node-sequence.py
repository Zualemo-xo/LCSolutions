class Solution(object):
    def maximumScore(self, A, edges):
        n = len(A)
        G = [[] for i in range(n)]
        for i,j in edges:
            G[i].append([A[j], j])
            G[j].append([A[i], i])
        #print(G)
        for i in range(n):
            G[i] = nlargest(3, G[i]) #for each row, sort 3 max elem alone in desc order
        #print(G)
        res = -1
        for i,j  in edges:
            for vii, ii in G[i]:
                for vjj, jj in G[j]:
                    if ii != jj and ii != j and jj != i:
                        res = max(res, vii + vjj + A[i] + A[j])
        return res