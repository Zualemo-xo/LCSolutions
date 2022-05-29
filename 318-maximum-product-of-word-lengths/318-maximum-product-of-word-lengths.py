class Solution:
    def maxProduct(self, words: List[str]) -> int:
        #Hash table: d[words][27]
        d=[[0 for i in range(27)] for j in range(len(words))]
        #print(d)
        #fill HT
        for i in range(0,len(words)):
            for j in words[i]:
                d[i][ord(j)-97]+=1
        
        ans=0
        #check for max
        
        for i in range(0,len(d)):
            for j in range(i+1,len(d)):
                flag=0
                for k in range(0,27):
                    if(d[i][k]>0 and d[j][k]>0):
                        flag=-1
                        break
                        
                if(flag==-1):
                    continue
                else:
                    ans=max(ans,sum(d[i])*sum(d[j]))
        
        return(ans)
                
            