class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        fac=len(columnTitle)-1
        ans=0
        for i in range(0,len(columnTitle)):
            ans=ans+(ord(columnTitle[i])-64)*(26**fac) #inc. by a factor of tot. english letters
            fac-=1
        return(ans)
        