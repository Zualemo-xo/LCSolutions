class Solution:
    def bitwiseComplement(self, N: int) -> int:
        c = 1
        while c < N: 
            c = (c << 1) + 1
            print(c)
        return N ^ c