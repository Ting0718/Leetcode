'''two arrays solution'''
class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = []
        res = 0

        # get maxLeft
        mLeft = 0
        for i in range(len(height)):
            maxLeft.append(mLeft)
            mLeft = max(mLeft, height[i])

        # get maxRight
        mRight = 0
        for i in range(len(height) - 1, -1, -1):
            maxRight.append(mRight)
            mRight = max(mRight, height[i])

        maxRight.reverse()  # need to reverse max right

        for i in range(len(maxRight)):
            minimum = min(maxRight[i], maxLeft[i])
            if minimum - height[i] > 0:
                res += minimum - height[i]

        return res


'''two pointers solution'''
class Solution:
    def trap(self, height: List[int]) -> int:
        # find the max left and max right of e, and take min(L, R)
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res
