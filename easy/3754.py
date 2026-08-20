class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sod = 0
        x = ""

        if n == 0:
            return 0

        for ch in str(n):
            if ch == '0':
                continue
            
            x += ch
            sod += int(ch)
        

        return int(x) * sod


            
        