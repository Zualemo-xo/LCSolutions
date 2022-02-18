class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack=deque(num[0]) #the implementation is optimized for front- and back- operations. push,pop at end and start of deque,Optimized for O(1),lists its O(N)
        for i in range(1,len(num)):
            #print(stack)
            #print(int(stack[-1]),int(num[i]))
            while(len(stack)!=0 and int(stack[-1])>int(num[i]) and k>0  ):
                stack.pop()
                k-=1
            stack.append(num[i])
        while(k>0): # incase all elem are non-decreasing 
            stack.pop()
            k-=1
        while(len(stack)!=0 and stack[0]=="0"): #leading zeroes removal
            stack.popleft()
        if(len(stack)==0): # we have to return 0 if all elem are removed
            stack.append("0")
        return(''.join(stack))
                
        
        
        