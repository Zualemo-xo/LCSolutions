class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        queue = []
        visited = set()
        courses_needed = defaultdict(int)

        def addQueue():
            for i in range(0,len(courses_needed)):
                if(courses_needed[i] == 0):
                    queue.append(i)

        adj_matrix = [[0 for i in range(0,numCourses+1)] for j in range(0,numCourses+1)]
        for course in prerequisites:
            adj_matrix[course[0]][course[1]] = 1
        
        for i in range(0,len(adj_matrix)):
            courses_needed[i] = sum(adj_matrix[i])

        addQueue()
        #BFS
        while(len(queue) != 0):
            
            ele = queue.pop()
            if(ele not in visited):
                visited.add(ele)
                for i in range(0,len(adj_matrix)):
                    if(adj_matrix[i][ele] == 1):
                        adj_matrix[i][ele] = 0 # since this course has been taken , no more a prerequisite
                        courses_needed[i]-=1
                addQueue()
        
        if(len(visited)-1 == numCourses):
            return(True)
        else:
            return(False)
            







        