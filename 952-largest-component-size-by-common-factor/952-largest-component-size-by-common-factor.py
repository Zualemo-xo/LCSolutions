class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        self.parent=[]
        def initialize(size):
            for i in range(size):
                self.parent.append(i) #Link every number till max with itself(by assigning it to its index pos)
        
        def getAbsoluteParent(i):
            if(self.parent[i]==i):
                return(i)
            else:
                self.parent[i]=getAbsoluteParent(self.parent[i]) #recusre till main parent ele is found
                return(self.parent[i])
        
        def unify(i,j):
            AbsoluteParenti=getAbsoluteParent(i)
            AbsoluteParentj=getAbsoluteParent(j)
            
            if(AbsoluteParenti!=AbsoluteParentj):
                # 7->2, 21->2 (7,21)
                self.parent[AbsoluteParentj]=AbsoluteParenti
        
        #main fn
        #Find max
        maxn=max(nums)
        initialize(maxn+1) #create parent array
        
        for i in nums:
            for j in range(2,i,1):
                if(j*j>i): #reduces TC
                    break
                if(i%j==0): # j is a factor of i
                    unify(j,i) # i=21, j=3
                    unify(i//j,i) # (21,3), (21,21/3(7))
        
        #dict to store the components along with their size, to find the maximum component
        d=defaultdict(int)
        for i in nums:
            parent= getAbsoluteParent(i) #Bada parent like 2 retrieved
            d[parent]+=1 #increase its size count by 1
        maxComponent= max(d.values()) #Fetch component with maximum size
        return(maxComponent)
	                