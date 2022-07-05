class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # O(N) TC,SC USING STACKS, TO POP WHEN NGE IS SEEN
        stack=deque([])
        positions=[-1]*len(nums)
        #d=defaultdict(int)
        n=len(nums)
        for i in range(0,2*n):
            k=nums[i%n]
            if(len(stack)==0):
                stack.append((i%n,k))
            else:
                while(len(stack)!=0 and stack[-1][1]<k):
                    pos,ele=stack.pop()
                    positions[pos]=k
                stack.append((i%n,k))
        

        return(positions)