'''Solution 2: Use an Array'''
from collections import defaultdict
class Solution(object):
    def findJudge(self, n, trust):
        if n - 1 > len(trust):
            return -1

        trust_scores = [0] * (n + 1)

        for a, b in trust:
            trust_scores[a] -= 1
            trust_scores[b] += 1

        for i in range(1, len(trust_scores)):
            if trust_scores[i] == n - 1:
                return i

        return -1

'''Solution 1: Use HashMap and Array'''
class Solution(object):
    def findJudge(self, n, trust):
        if not trust:
            if n - 1 > len(trust):
                return -1
            return n

        hashMap = defaultdict(int)
        persons = []
        for p, t, in trust:
            persons.append(p)
            hashMap[t] += 1

        candidate, num_of_trust = max(hashMap.items(), key=lambda x: x[1])
        if candidate in persons or num_of_trust != n - 1:
            return -1
        else:
            return candidate
