
'''sort function'''
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

'''normal dictionary'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        visited = {}
        for i in range(len(s)):
            if s[i] not in visited:
                visited[s[i]] = 1
            else:
                visited[s[i]] += 1

            if t[i] not in visited:
                visited[t[i]] = -1
            else:
                visited[t[i]] -= 1

        for i in visited:
            if visited[i] != 0:
                return False

        return True

'''dictionary using counter'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = Counter(s)
        dict_t = Counter(t)
        
        return dict_s == dict_t

'''use counter as dictionary'''
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = Counter(s)
        dict_t = Counter(t)
        
        return dict_s == dict_t


'''use defaultdict'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        visited = defaultdict(int)
        for i in range(len(s)):
            visited[s[i]] += 1
            visited[t[i]] -= 1

        for i in visited:
            if visited[i] != 0:
                return False

        return True
