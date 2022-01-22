class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0  # last 2 houses we rob

        # [rob1, rob2, n, n + 1, ...]
        for n in nums:
            # if i want to rob n, i also need to rob1 as well
            tmp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tmp

        return rob2  # the max to rob
