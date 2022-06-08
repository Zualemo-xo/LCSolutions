class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #DFS
        self.cnt=0
        self.ans=[]
        def dfs(node,track):
            if(node==len(graph)-1):
                self.cnt+=1
                self.ans.append(track)
                return
            for i in graph[node]:
                dfs(i,track+[i])

            
        dfs(0,[0])
        print(self.cnt)
        return(self.ans)