class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return 0

        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        s = sorted(d.values())
        index, count = 0, 0
        while k > 0:
            k -= s[index]
            index += 1

        if k == 0:
            return len(s) - index
        else:
            return len(s) - index + 1