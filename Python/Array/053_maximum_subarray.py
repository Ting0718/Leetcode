class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = max_global = nums[0]
        for i in range(1, len(nums)):  # 0 is initialized, start from 1
            max_current = max(max_current + nums[i], nums[i])
            max_global = max(max_current, max_global)
        return max_global

        
'''Brute Force'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = 0
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)

        return max_sum



