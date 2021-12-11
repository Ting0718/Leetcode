class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            if i >= 0:
                Aleft = A[i]
            else:
                Aleft = float("-inf")

            if (i + 1) < len(A):
                Aright = A[i + 1]
            else:
                Aright = float("inf")

            if j >= 0:
                Bleft = B[j]
            else:
                Bleft = float("-inf")

            if (j + 1) < len(B):
                Bright = B[j + 1]
            else:
                Bright = float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Bright, Aright)
                else:
                    return (max(Bleft, Aleft) + min(Bright, Aright)) / 2

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1