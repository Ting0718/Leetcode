'''interative solution'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1

'''Recursion'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(l, r):
            if l > r:
                return -1
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return helper(l, mid - 1)
            else:
                return helper(mid + 1, r)

        return helper(0, len(nums) - 1)