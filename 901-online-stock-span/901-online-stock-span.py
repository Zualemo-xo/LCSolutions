class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        cnt=1
        if(len(self.stack)==0): #First time fn is called
            self.stack.append([price,cnt])
            return(cnt)
        while(len(self.stack)!=0 and price>=self.stack[-1][0]): #All other times,pop elem till greater price is encountered, and add the popped elements cnt
            cnt+=self.stack.pop()[1]
        self.stack.append([price,cnt])
        return(cnt)


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)