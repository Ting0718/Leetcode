class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = nums[left] + nums[right] + nums[i]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([nums[left], nums[right], nums[i]])
                    left += 1
                    while nums[left - 1] == nums[left] and left < right:
                        left += 1

        return res
