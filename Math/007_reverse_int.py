class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0] == "-":
            a = int(str(x)[0]+str(x)[1:][::-1])
            if a < -2**31: 
                return 0
            return a
        else:
            a = int(str(x)[::-1])
            if a > (2**31) - 1:
                return 0
            return a