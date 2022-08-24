class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        power=round( log(sys.maxsize,3) ) 
        maxval=3**power
        print(maxval%27)
        return(n>0 and maxval%n==0)