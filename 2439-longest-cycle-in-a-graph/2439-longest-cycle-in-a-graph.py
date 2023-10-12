class Solution(object):
    maxCycle = -1
    def dfs(self, i, Edge, visited, maxCycle ):
        dist = defaultdict(int)
        if(i not in visited and Edge[i] !=-1):
            dist[i] = 1
            curNode = i
            #print(curNode)
            while(Edge[curNode]!=-1 and Edge[curNode] not in visited):
                visited.add(curNode)
                dist[Edge[curNode]] = dist[curNode] + 1 
                curNode = Edge[curNode]
                
            if(Edge[curNode] != -1 and Edge[curNode] in dist): # meaning a visited node is encountere ALA cycle found.
                if(dist[curNode] - dist[Edge[curNode]] + 1  > self.maxCycle): # subtract current node distance with repeating node's dist
                    self.maxCycle = dist[curNode] - dist[Edge[curNode]] + 1 
    def longestCycle(self, Edge):
        """
        :type edges: List[int]
        :rtype: int
        """
        visited = set()

        for i in range(0,len(Edge)):
            #dfs
            self.dfs(i, Edge, visited, self.maxCycle)
            
        return(self.maxCycle)
        