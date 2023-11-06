class SeatManager:

    def __init__(self, n: int):
        self.unreserved = []
        for i in range(1,n+1):
            self.unreserved.append(i)
        heapq.heapify(self.unreserved)
        

    def reserve(self) -> int:
        num = heapq.heappop(self.unreserved)
        return(num)
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unreserved, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)