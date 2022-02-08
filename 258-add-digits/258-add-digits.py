
class Solution(object):
    def addDigits(self, num):
        l=list(str(num))
        while(num>9):
            num=0
            for i in range(0,len(l)):
                num+=int(l[i])
            l=list(str(num))
        return(num)