class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf")
        for i in range(len(nums)-1):
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[l] + nums[r] + nums[i]
                if three_sum == target:
                    return three_sum

                if abs(target - three_sum) < abs(target - closest):
                    closest = three_sum

                elif three_sum < target:
                    l += 1
                else:
                    r -= 1
        return closest
