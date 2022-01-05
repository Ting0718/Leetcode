class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure that abs(a) >= abs(b)
        if x < y:
            return self.getSum(b, a)

        if a > 0:
            sign = 1
        else:
            sign = -1

        if a * b >= 0:
            while y:
                tmp = (x & y) << 1
                x = x ^ y
                y = tmp
        else:
            while y:
                tmp = (~x & y) << 1
                x = x ^ y
                y = tmp

        return x * sign
