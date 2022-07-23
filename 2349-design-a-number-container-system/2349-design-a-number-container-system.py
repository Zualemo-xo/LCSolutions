from sortedcontainers import SortedList
class NumberContainers:

    def __init__(self):
        self.ind=defaultdict(int)
        self.mini=defaultdict(lambda: SortedList())
        
    def change(self, index: int, number: int) -> None:
        change=-1
        if(index in self.ind):
            change=self.ind[index]
            
        self.ind[index]=number
        # if(number not in self.mini):
        #     self.mini[number]=[]
        self.mini[number].add(index)
        #print(self.mini)
        
        if(change!=-1):
            i=self.mini[change].index(index)
            self.mini[change].pop(i)
            #print(self.mini[change])
            #heapq.heapify(self.mini[change])
        return(0)

    def find(self, number: int) -> int:
        if(number not in self.mini or len(self.mini[number])==0):
            return(-1)

        return(self.mini[number][0])
        #return(0)


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)