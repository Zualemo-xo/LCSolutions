class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)<3 or A[0]>=A[1]:
            return False
        inc=True
        for i in range(1,len(A)+1):
            if(i==len(A)):
                if(inc==False):
                    return(True)
                break #else if only increasig
            
            if(A[i-1]==A[i]): #not strictly inc
                break
            if(A[i-1]>A[i]): #increasing till peak
                inc=False
            
            elif(A[i-1]<=A[i] and inc==False): #while decreasing if there is a increase
                break
        return(False) #all breaks leads to