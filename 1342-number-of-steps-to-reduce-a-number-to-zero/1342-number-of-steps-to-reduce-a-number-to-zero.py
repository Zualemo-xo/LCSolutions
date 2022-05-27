class Solution:
    def numberOfSteps(self, num: int) -> int:
        #Simulate
        cnt=0
        print("New")
        while(num!=0):
            cnt+=1
            print(bin(num))
            num=num//2 if num%2==0 else num-1
        return(cnt)