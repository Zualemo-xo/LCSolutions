class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        x=bin(num)[2:]
        x1=""
        for i in range(0,len(x)):
            if(x[i]=="0"):
                x1+="1"
            else:
                x1+="0"
        return(int(x1,2))
        