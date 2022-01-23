class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans=[]
        for i in range(len(str(low)),len(str(high))+1):
            for j in range(1,10):
                t=""
                outt=False
                for k in range(0,i):
                    if(j+k>=10):
                        outt=True
                        break
                    t+=str(j+k)
                if(outt):
                    break
                #print(t)
                if(int(t)>=low and int(t)<=high):
                    ans.append(int(''.join(t)))
        return(ans)
                    