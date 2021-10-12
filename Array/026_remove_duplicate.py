class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        while index < len(nums)-1:
            if nums[index] == nums[index+1]:
                nums.pop(index)
            else:
                index += 1

        return len(nums)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[l] = nums[i+1]
                l += 1
        return l



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        if len(nums) == 0:
            return length
        for i in range(1, len(nums)):
            if nums[length] < nums[i]:
                length += 1
                nums[length] = nums[i]

        return length + 1
