class Solution:
    def integerBreak(self, n: int) -> int:
        quotient = n//3
        remainder = n%3
        if(n == 2):
            return(1)
        elif(n == 3):
            return(2)
        if(remainder == 1):
            return(((3)**(quotient-1))*4)
        elif(remainder == 2):
            return(((3)**quotient)*2)
        elif(remainder == 0):
            return(3**quotient)


        