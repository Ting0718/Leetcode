class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sum = {0: 1}
        current_sum = 0

        for n in nums:
            current_sum += n
            diff = current_sum - k

            res += prefix_sum.get(diff, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        return res
