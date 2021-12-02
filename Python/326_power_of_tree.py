class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 3 == 0:
            n = n // 3

        return n == 1


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True

        expo = 1
        res = 0
        while res < n:
            res = 3**expo
            expo += 1
            if res == n:
                return True

        return False
