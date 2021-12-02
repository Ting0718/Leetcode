'''Better Solution'''
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        current_str = ""
        max_count = 0

        for i in range(len(s)):
            if s[i] not in current_str:
                current_str += s[i]
                d[s[i]] = i
                max_count = max(max_count, len(current_str))
            else:
                current_str = s[d[s[i]] + 1: i + 1]
                d[s[i]] = i
                max_count = max(max_count, len(current_str))

        return max_count

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = dict()
        max_length = 0
        current_str = ""
        for i in range(len(s)):
            if s[i] not in current_str:
                hashmap[s[i]] = i
                current_str += s[i]
                max_length = max(max_length, len(current_str))
            else:
                current_str = s[hashmap[s[i]]+1:i] + s[i]
                hashmap[s[i]] = i
                max_length = max(max_length, len(current_str))

        return max_length
