class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        shiftcnt=0
        while(left!=right):
            print(left,right)
            left>>=1
            right>>=1
            shiftcnt+=1
        return(left<<shiftcnt)
        