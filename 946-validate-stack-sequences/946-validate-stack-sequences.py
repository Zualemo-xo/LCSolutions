class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack=deque()
        pop_pos=0
        for i in pushed:
            stack.append(i)
            while(len(stack)!=0 and popped[pop_pos]==stack[-1]):
                stack.pop()
                pop_pos+=1
                print(pop_pos)
        if(pop_pos!=len(popped)):
            return(False)
        else:
            return(True)