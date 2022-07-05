class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # O(N) TC,SC USING STACKS, TO POP WHEN NGE IS SEEN
        stack=deque([])
        #positions=[-1]*len(nums)
        d=defaultdict(int)
        for i in nums2:
            if(len(stack)==0):
                stack.append(i)
            else:
                while(len(stack)!=0 and stack[-1]<i):
                    ele=stack.pop()
                    d[ele]=i
                stack.append(i)
        
        ans=[]
        #print(d)
        for i in nums1:
            if(i in d):
                ans.append(d[i])
            else:
                ans.append(-1)
        return(ans)