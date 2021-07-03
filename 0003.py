def lengthOfLongestSubstrings(s: str) -> int:
    s1 = ""
    temp = ""
    for i in range(len(s)):
        for j in range(len(s[i:])):
            if temp.find(s[j]) == -1:
                temp += s[j]
                if len(temp) > len(s1):
                    print(temp)
                    s1 = temp
            else:
                temp = ""
                break
    return len(s1)


print(lengthOfLongestSubstrings("pwwkew"))
