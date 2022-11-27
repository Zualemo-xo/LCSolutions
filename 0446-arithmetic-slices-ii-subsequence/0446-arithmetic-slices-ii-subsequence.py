class Solution(object):
    def numberOfArithmeticSlices(self, A):
        from collections import defaultdict
        total = 0
        dp = [defaultdict(int) for item in A]
        for i in xrange(len(A)):
            for j in xrange(i):
                dp[i][A[i] - A[j]] += 1
                if A[i]-A[j] in dp[j]:
                    dp[i][A[i] - A[j]] += dp[j][A[i]-A[j]]
                    total += dp[j][A[i]-A[j]]
        return total
        