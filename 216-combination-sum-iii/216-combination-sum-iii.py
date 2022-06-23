class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        #Backtracking
        self.ans=[]
        def backtrack(arr,sizeleft,sumarr,start):
            if(sizeleft==0):
                if(sumarr==n):
                    #print(arr)
                    self.ans.append(list(arr))
                else:
                    return
            elif(sumarr>n):
                return
            else:
                for i in range(start,10):
                    arr.append(i)
                    backtrack(arr,sizeleft-1,sumarr+i,i+1)
                    arr.pop()
        backtrack([],k,0,1)
        return(self.ans)
                    