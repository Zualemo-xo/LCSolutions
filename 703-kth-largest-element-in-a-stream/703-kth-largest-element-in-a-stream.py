from heapq import heappush,heappop,heapify,nlargest,heapreplace
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.l=[]
        self.k=k
        heapify(self.l)
        for i in nums:
            if(len(self.l)<self.k):
                heappush(self.l,i)
            elif(self.l[0]<=i): 
                heapreplace(self.l,i)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if(len(self.l)<self.k):
            heappush(self.l,val)
        elif(self.l[0]<=val): #if there are k elem in PQ, push only if the new elem is greater than self.l[0]
            heapreplace(self.l,val) #pop smallest val,push new big val 
        return(self.l[0] if len(self.l)==self.k else -1)
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)