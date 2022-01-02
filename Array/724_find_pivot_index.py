'''Brute Force'''
class Solution(object):
    def pivotIndex(self, nums):
        if not nums:
            return -1
        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            if i == 0:  # first element
                if sum(nums[i+1:]) == 0:
                    return i
            elif i == len(nums) - 1:
                if sum(nums[:i]) == 0:
                    return i
            else:
                if sum(nums[:i]) == sum(nums[i+1:]):
                    return i

        return -1

'''prefix and postfix sum'''
class Solution(object):
    def pivotIndex(self, nums):
        prefix = []
        postfix = []

        pre = 0
        for n in nums:
            prefix.append(pre)
            pre += n

        post = 0
        for n in nums[::-1]:
            postfix.append(post)
            post += n

        postfix = postfix[::-1]
        for i in range(len(prefix)):
            if prefix[i] == postfix[i]:
                return i
        return -1

'''use left right sum'''
class Solution(object):
    def pivotIndex(self, nums):
        leftsum = 0
        rightsum = sum(nums)
        for i in range(len(nums)):
            rightsum -= nums[i]
            if leftsum == rightsum:
                return i

            leftsum += nums[i]

        return -1
