class Solution:
    ##ddbabichev way queue 1..10 then get 12,13, from 1,2 and so on....
    def sequentialDigits(self, low, high):
        out = []
        queue = deque(range(1,10))
        while queue:
            elem = queue.popleft()
            if low <= elem <= high:
                out.append(elem)
            last = elem % 10
            if last < 9: queue.append(elem*10 + last + 1)
                    
        return out
        