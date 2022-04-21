class MyHashSet:

    def __init__(self):
        self.x=[]

    def add(self, key: int) -> None:
        self.x.append(key)

    def remove(self, key: int) -> None:
        
        for i in range(len(self.x)):
            if(self.x[i]==key):
                self.x[i]=-1
        #print(self.x)

    def contains(self, key: int) -> bool:
        if(key in self.x):
            #print(self.x.index(key))
            return(True)
        return(False)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)