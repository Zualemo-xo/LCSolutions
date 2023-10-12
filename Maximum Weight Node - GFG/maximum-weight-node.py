#User function Template for python3
from collections import defaultdict
class Solution():
    def maxWeightCell(self, N, Edge):
        d = defaultdict(int)
        for i in range(0,len(Edge)):
            if(Edge[i]!=-1):
                d[Edge[i]] += i
        max_weight, cell = 0,0
        
        for i in d:
            if(d[i]>max_weight ):
                max_weight = d[i]
                cell = i
            elif(d[i] == max_weight and i>cell):
                cell = i
        return(cell)
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        Edge = [int(i) for i in input().split()]
        obj = Solution()
        ans=obj.maxWeightCell(N, Edge);
        print(ans)

# } Driver Code Ends