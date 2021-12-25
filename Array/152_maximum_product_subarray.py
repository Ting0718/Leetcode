class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        current_min, current_max = 1, 1

        for n in nums:
            tmp = current_max * n
            current_max = max(n * current_max, n * current_min, n)
            current_min = min(tmp, n * current_min, n)
            res = max(current_max, res)

        return res
