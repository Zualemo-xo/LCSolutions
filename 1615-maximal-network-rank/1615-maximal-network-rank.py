import heapq
class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adj=defaultdict(list)
        l=[]
        for i in range(n):
            l.append([0,i]) #[count,node_index]
        
        for u,v in roads:
            adj[u].append(v)
            adj[v].append(u)
            l[u][0]-=1 #- for maxheap
            l[v][0]-=1
        heapq.heapify(l)  
        
        #print(l,adj)
        maxcnt,max2cnt,firsttime=[],[],0
        while(len(l)!=0):
            x1=heapq.heappop(l)
            x2=[-1,-1]
            if(len(l)!=0):
                x2=heapq.heappop(l)
            if(firsttime==0 and x1[0]!=x2[0]):
                maxcnt.append(x1)
            
            elif(x1[0]==x2[0] and len(maxcnt)==0):
                maxcnt.append(x1)
                maxcnt.append(x2)
            elif(x1[0]==x2[0] and x1[0]==maxcnt[-1][0]):
                maxcnt.append(x1)
                maxcnt.append(x2)
            elif(x1[0]>x2[0] and x1[0]==maxcnt[-1][0]):
                maxcnt.append(x1)
            else:
                break
            firsttime+=1
            # x1[0] -- count , x1[1] -- position/node
        #print(maxcnt)
        ans,tans=0,0
        for ele in maxcnt:
            tans=-ele[0] # add this sum
            for i in adj:
                if(i!=ele[1]):
                    tans=-ele[0] 
                    tans+=len(adj[i])
                    if(ele[1] in adj[i]):
                        tans-=1
                    ans=max(ans,tans)
        return(ans)
            
            
        
        