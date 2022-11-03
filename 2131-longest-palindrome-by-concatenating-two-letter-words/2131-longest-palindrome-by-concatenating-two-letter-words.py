class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        eqcnt,cnt=0,0
        deq=defaultdict(int)
        d=defaultdict(int)
        dsort=defaultdict(int)
        for i in words:
            if(i==i[::-1]):
                eqcnt+=1
                deq[i]+=1
            # elif(i in d.keys() ):
            #     #print("fu")
            #     d[i]+=1
            if(''.join(sorted(i))== i  ):
                dsort[i]+=1
            elif(''.join(sorted(i))!= i  ):
                d[''.join(sorted(i))]+=1

        print(d)
        print(deq)
        print(dsort)
        single=False
        maxrep=0
        for i in deq:
            
            if(i==i[::-1]):
                if(deq[i]==1 or deq[i]%2==1):
                    #maxrep=max(maxrep,1)
                    single=True
                #else:
                maxrep+=deq[i]//2
        for i in dsort:
            if(dsort[i]==d[i]):
                cnt+=(dsort[i]+d[i])//2
            else:
                cnt+=min(dsort[i],d[i])
        
        #print(maxrep,eqcnt)
        if(single==True):
            return(cnt*2*2+maxrep*2*2+2) 
        return(cnt*2*2+maxrep*2*2)