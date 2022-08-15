class Solution:
    def romanToInt(self, s: str) -> int:
        ans=0
        s+="-1"
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        #for i in range(0,len(s),1):
        i=0
        while(i<len(s)):
            #print(i,s[i])
            if(s[i]=="I"):
                if(s[i+1]=="V" or s[i+1]=="X"):
                    ans+=d[ s[i+1] ] - d[ s[i] ]
                    i+=2
                else:
                    ans+=d[ s[i] ]
                    i+=1
                    
            elif(s[i]=="X"):
                if(s[i+1]=="L" or s[i+1]=="C"):
                    ans+=d[ s[i+1] ] - d[ s[i] ]
                    i+=2
                else:
                    ans+=d[ s[i] ]
                    i+=1
                    
            elif(s[i]=="C"):
                #print("coc")
                if(s[i+1]=="D" or s[i+1]=="M"):
                    ans+=d[ s[i+1] ] - d[ s[i] ]
                    #print("ans",ans)
                    i+=2
                    #print(i)
                else:
                    ans+=d[ s[i] ]
                    i+=1
                    
            elif(s[i] in d):
                ans+=d[ s[i] ]
                i+=1
            else:
                i+=1
        
        return(ans)
                    