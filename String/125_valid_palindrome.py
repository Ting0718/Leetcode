class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum()).lower()

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        n_str = ""
        for i in s:
            if i.isalnum():
                n_str += i.lower()

        return n_str == n_str[::-1]

        s = "".join(c for c in s if c.isalnum()).lower()
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


'''
a = "abcdefghijklmnopqrstuvyxyz1234567890"
n_string = ""
for i in s: 
    if i != " " and i.lower() in a:
        n_string += i.lower()

if n_string.strip() == "":
    return True
return n_string == n_string[::-1]
'''
