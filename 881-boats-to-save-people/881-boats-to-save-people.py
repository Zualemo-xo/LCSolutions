class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        f,b,cnt=0,len(people)-1,0
        while(f<b):
            if(people[f]+people[b]<=limit):
                print(people[f],people[b])
                cnt+=1
                f+=1
            b-=1
        return(cnt+len(people)-(2*cnt))