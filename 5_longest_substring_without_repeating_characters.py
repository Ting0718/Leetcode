class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        usedChar = {}
        start = maxLength = 0
        for i, c in enumerate(s):
            if c in usedChar and start <= usedChar[c]:
                # always updates the position of last repeated digits
                start = usedChar[c] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[c] = i

        return maxLength


# create a helper method -> slow


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        for i in range(len(s)):
            maxLength = max(maxLength, self.helper(s, i))

        return maxLength

    def helper(self, string, start):
        seen = set()
        for i in range(start, len(string)):
            if string[i] not in seen:
                seen.add(string[i])
            else:
                return i - start

        return len(string) - start


'''another solution'''
    m = ''  # Memory to remember a palindrome
    for i in range(len(s)):  # i = start, O = n
        for j in range(len(s), i, -1):  # j = end, O = n^2
            if len(m) >= j-i:  # To reduce time
                break
            elif s[i:j] == s[i:j][::-1]:
                m = s[i:j]
                break
    return m
