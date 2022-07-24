class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #ROW ITER+ BINARY SEARCH  TC: (M log N), M- rows N-cols, SC: O(1)
        for row in (matrix):
            low,high=0,len(row)-1
            
            
            while(low<=high):
                mid=(low+high)//2
                
                if(row[mid]==target):
                    return(True)
                elif(target<row[mid]):
                    high=mid-1
                else:
                    low=mid+1
        return(False)
        