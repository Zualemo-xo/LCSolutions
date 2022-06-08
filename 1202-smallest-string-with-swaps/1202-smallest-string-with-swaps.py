import heapq
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.parent=[]
        def initialize(n):
            for i in range(n):
                self.parent.append(i)
        
        def getAbsoluteParent(i):
            if(self.parent[i]==i):
                return(i)
            else:
                self.parent[i]=getAbsoluteParent(self.parent[i])
                return(self.parent[i])
        
        def union(i,j):
            AbsoluteParenti = getAbsoluteParent(i)
            AbsoluteParentj = getAbsoluteParent(j)
            
            if(AbsoluteParenti!= AbsoluteParentj):
                self.parent[AbsoluteParentj]=AbsoluteParenti
        #Main
        initialize(len(s))
        
        for i in pairs:
            union(i[0],i[1])
        # 2 dicts 
        groups=defaultdict(list) # {absoluteParent:[words]}
        AbsoluteParent=defaultdict(int) #{Number: AbsoluteParent} this is used to access 'groups'
        for i in range(len(self.parent)):
            AP=getAbsoluteParent(i)
            groups[AP].append(s[i])
            AbsoluteParent[i]=AP
        
        for i in groups:
            groups[i].sort() #sort based on alphabetical order for each  group
        #print(self.parent)
        #print(groups)
        #print(AbsoluteParent)
        
        ans=""
        # Get answer based on smallest sorted letter in its parent group
        for i in range(0,len(s)):
            AP=AbsoluteParent[i]
            sorted_grp_letter=groups[AP].pop(0)
            ans+=sorted_grp_letter
        return(ans)