class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        l=[]
        minz=float("inf")
        arr.sort()
        for i in range(1,len(arr)):
            if(arr[i]-arr[i-1]<minz):
                minz=arr[i]-arr[i-1]
                
        for i in range(1,len(arr)):
            if(arr[i]-arr[i-1]==minz):
                l.append([arr[i-1],arr[i]])
        return(l)