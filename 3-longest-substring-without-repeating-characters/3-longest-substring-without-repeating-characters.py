class Solution:
    def lengthOfLongestSubstring(self, n: str) -> int:
        #sliding window
        slidingw=deque([])
        s=set()
        maxl=0
        for i in n:
            if(i in s):
                while(len(slidingw)!=0):
                    ele=slidingw.popleft()
                    s.remove(ele)
                    if(ele==i):
                        break
                s.add(i)
                slidingw.append(i)
                
            else:
                s.add(i)
                slidingw.append(i)
                maxl=max(maxl,len(slidingw))
                #print(slidingw,maxl)
        return(maxl)
                