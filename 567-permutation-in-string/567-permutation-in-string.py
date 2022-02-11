
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1=defaultdict(int)
        for i in s1:
            d1[i]+=1
        #print(d1)
        d2=defaultdict(int)
        for i in range(0,len(s2)):
            #print(sum(d2.values()))
            if(sum(d2.values())<len(s1)-1):
                d2[s2[i]]+=1
            else:
                d2[s2[i]]+=1
                #print("fdd:",d2)
                cnt=0
                for j in d1:
                    #print(j,d2)
                    if(j in d2 and d1[j]==d2[j]):
                        cnt+=1
                        continue
                    else:
                        break
                    #print("done")
                    return(True)
                if(cnt==len(d1)):
                    return(True)
                #print(d2,d2[s2[i-len(s1)+1]])
                d2[s2[i-len(s1)+1]]-=1
                if(d2[s2[i-len(s1)+1]]==0):
                    d2.pop(s2[i-len(s1)+1])
        return(False)
                
        
        