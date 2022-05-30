class Solution(object):
    def divide(self, dividend, divisor):
        return(int(ceil(float(dividend)/float(divisor))) if( (dividend/divisor)<0 ) else min(2147483647,dividend/divisor) )  