class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #TOPO SORT
        adj_list=defaultdict(list)
        #outgoing_cnt=defaultdict(int)
        incoming_cnt=defaultdict(int)
        #print(adj_list)
        
        #Creation of Adj list, count of outgoing nodes
        for i in prerequisites:
            adj_list[i[1]].append(i[0])
            #outgoing_cnt[i[1]]+=1
            incoming_cnt[i[0]]+=1
        #print(outgoing_cnt)
        #print(adj_list)
        
        #Store nodes with no outgoing edges into queue
        queue=deque([])
        ans=[]
        for i in range(numCourses):
            if(i not in incoming_cnt):
                #print(i)
                queue.append(i)
        #Main topo sort processing
        while(len(queue)!=0):
            #print(queue)
            course=queue.popleft()
            for dep in adj_list[course]:
                incoming_cnt[dep]-=1 #we have visited its prerequesite course , hence remove its incoming connection to 'dep'
                if(incoming_cnt[dep]==0): # we can now take this subject
                    queue.append(dep)
            ans.append(course)
        
        if(len(ans)!=numCourses):
            return([])
        else:
            return(ans)
            
            
        
            
            