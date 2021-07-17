class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        index = 0
        while count < len(nums):
            if nums[index] == 0:
                nums.append(nums.pop(index))
            else:
                index += 1

            count += 1
