class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d=defaultdict(int)
        
        for i in arr:
            d[i]+=1
        pq=[]
        heapq.heapify(pq)
        for i in d:
            heapq.heappush(pq,-d[i])
        cnt,sumz=0,0
        n=len(arr)
        while(len(pq)!=0):
            if(sumz>=n//2):
                break
            ele=heapq.heappop(pq)
            sumz-=ele
            cnt+=1
        return(cnt)
        