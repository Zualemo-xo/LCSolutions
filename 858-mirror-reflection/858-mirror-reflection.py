class Solution:
    def mirrorReflection(self, p, q):
        k = 1
        while k*q%p: k += 1
        return 2 if k%2==0 else (k*q//p)%2
        