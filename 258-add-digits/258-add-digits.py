
class Solution(object):
    def addDigits(self, num):
        return 1 + (num - 1) % 9 if num else 0
        # Testing pattern between 0 and 100..we observe 0 , then 1-9 repeating
        # for num in range(0,100):
        #     l=list(str(num))
        #     while(num>9):
        #         num=0
        #         for i in range(0,len(l)):
        #             num+=int(l[i])
        #         l=list(str(num))
        #     #return(num)
        #     print(num)