class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


class Solution:
    def hammingWeight(self, n: int) -> int:
        # O(32) = O(1)
        res = 0
        while n:
            res += n & 1
            n = n >> 1
        return res
