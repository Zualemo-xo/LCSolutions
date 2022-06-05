class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        self.ans=[]
        # whe check and add different positions into curr
        def backtrack(curr,pos):
            #print(curr,pos)
            #break condition
            if(len(curr)==n):
                tans=[]
                for i in curr:
                    tans.append(nums[i])
                if tans not in self.ans:
                    self.ans.append(tans)
                return

            #while(i%n!=pos%n):
            #loop from first ele and add if not already a position
            for i in range(0,n):
                if(i not in curr):
                    #print(i%n,pos%n)
                    curr.append(i)
                    backtrack(curr,i+1)
                    curr.pop()
                    #i+=1
        
        backtrack([],0)
        return(self.ans)