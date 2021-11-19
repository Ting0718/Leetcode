class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                p = p * -1
            else:
                p = p * 1

        return p
