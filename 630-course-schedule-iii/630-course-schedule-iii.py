import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # PQueue, TC: O(NlogN) SC: O(N) N: courses len
        courses.sort(key=lambda x:x[1]) #Sort by deadline
        selected=[]
        heapq.heapify(selected)
        print(courses)
        duration=0
        ans=0
        
        for coursetime,deadline in courses:
            #print(selected)
            if(duration+coursetime<=deadline):
                ans+=1
                duration+=coursetime
                heapq.heappush(selected,-coursetime) #- to implement maxheap
                continue
                #print(duration)
            #If current courseduration is less than max courseduration encountered till now,
            # pop out that maxCD and push current courseduration instead, ENSURES WE GET MAX no of courses
            #TC : [[10,12],[6,15],[1,12],[3,20],[10,19]]
            elif(len(selected)==0):
                continue
            largest=heapq.heappop(selected)
            if(coursetime<=-largest ):
                duration=duration-(-largest)+coursetime
                heapq.heappush(selected,-coursetime)
            else:
                heapq.heappush(selected,largest) 
        return(ans)
            