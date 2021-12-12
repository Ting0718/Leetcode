from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        count = sorted(Counter(s).values())
        res = 0
        count_set = set()

        for c in count:
            while c > 0 and c in count_set:
                c -= 1
                res += 1

            count_set.add(c)

        return res