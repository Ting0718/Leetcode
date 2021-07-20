class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = [i for i in range(1, len(nums)+1)]
        return set(a) - set(nums)
