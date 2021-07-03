'''
"string".index(element,start,end)

enumerate: useful for obtaining an indexed list: (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
'''


# https://leetcode.com/problems/two-sum/
'''brute force'''
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


'''bad solution'''
def twoSumR(nums: List[int], target: int) -> List[int]:
    l = 0
    n = nums
    while l < len(nums)-1:
        for i in range(1, len(n)):
            if n[0] + n[i] == target:
                return [nums.index(n[0]), nums.index(n[i], nums.index(n[0])+1)]
        l += 1
        n = nums[l:]


'''solutions online: faster to use hashmap (dictionary)'''
def twoSumR(nums: List[int], target: int) -> List[int]:
    seen = {}
    for index, num in enumerate(nums):
        other = target - num

        if other in seen:
            return [seen[other], index]

        else:
            seen[num] = index


