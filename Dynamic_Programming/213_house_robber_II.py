class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        # edge case: if the nums only has 1 house, take the only house nums[0]
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
