class Solution(object):
    def hammingWeight(self, n):
        return(collections.Counter( str(bin(n))[2:])['1'])