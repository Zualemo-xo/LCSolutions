import heapq
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # Using Heap TC: O(N.log(K)) SC: O(K)
        l=[ [-nums[0],0] ] #Maxheap
        #      value,index
        heapq.heapify(l)
        
        for i in range(1,len(nums)):
            while(True):
                ele=heapq.heappop(l)
                if(ele[1]<i-k): #This ele is out of range hence its val cannot be considered
                    continue
                heapq.heappush( l,[ele[0]-nums[i],i] )
                heapq.heappush( l,ele )
                break
        
        #print(l)
        while(True):
            ele=heapq.heappop(l)
            if(ele[1]!=len(nums)-1): #This ele is not last ele
                    continue
            else:
                return(-ele[0])