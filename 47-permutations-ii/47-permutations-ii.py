class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        self.ans=[]
        def backtrack(curr,pos):
            #print(curr,pos)
            if(len(curr)==n):
                tans=[]
                for i in curr:
                    tans.append(nums[i])
                if tans not in self.ans:
                    self.ans.append(tans)
                return

            #while(i%n!=pos%n):
            for i in range(0,n):
                if(i not in curr):
                    #print(i%n,pos%n)
                    curr.append(i)
                    backtrack(curr,i+1)
                    curr.pop()
                    #i+=1
        
        backtrack([],0)
        return(self.ans)