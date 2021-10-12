# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low,mid,high=0,n//2,n
        
        while(low<=high):
            
            mid=low+(high-low)//2
            x=guess(mid)
            if(x==0):
                return(mid)
            elif(x==-1):
                #n=mid-1
                high=mid-1
            else:
                #n=mid+1 initial mistake
                low=mid+1
            #print(high,low,mid)
            
        return(-1)