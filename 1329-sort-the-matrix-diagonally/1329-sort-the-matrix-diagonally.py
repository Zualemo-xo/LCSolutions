class Solution(object):
    def diagonalSort(self, A):
        m, n = len(A), len(A[0])
        def sort(i, j):
            ij = zip(range(i, m), range(j, n))
            vals = iter(sorted(A[i][j] for i, j in ij))
            for i, j in ij:
                A[i][j] = next(vals)
        for i in range(m): sort(i, 0)
        for j in range(n): sort(0, j)
        return A
