class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if(n==0):
            return([0])
        if(n==1):
            return([0,1])
        l=[0,1,1]
        for i in range(3,n+1):
            if(i%2!=0): #odd digit -- prev even digit+1 
                l.append(l[len(l)-1]+1)
            else: # even nos equivalent to shift of eve/2 digit ,so same 1 count
                l.append(l[len(l)/2])
        return(l)
                
        