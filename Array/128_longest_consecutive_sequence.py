class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in nums:
                length = 1
                while (n + length in nums):
                    length += 1

                longest = max(longest, length)

        return longest

'''Sorting'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        max_l = current_l = 1

        for i in range(1, len(nums)):
            n1 = nums[i - 1]
            n2 = nums[i]
            if n1 + 1 == n2 or n1 - 1 == n2:
                current_l += 1
                max_l = max(max_l, current_l)
            elif n1 == n2:
                pass
            else:
                current_l = 1

        return max_l