class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min_no = min(arr)
        max_no = max(arr)
        n = len(arr)
        if((max_no - min_no) % (n-1) != 0):
            return(False)
        ap = (max_no - min_no) // (n-1)
        if(ap == 0 and max_no == min_no ):
            return(True)
        elif(ap == 0):
            return(False)
        s = set(arr)
        for i in range(min_no,max_no+1,ap):
            if(i not in s):
                return(False)
        return(True)


        