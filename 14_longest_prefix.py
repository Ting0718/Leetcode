def longestCommonPrefix(self, strs: List[str]) -> str:
    if "" in strs:
        return ""
    elif len(strs) == 1:
        return strs[0]
    elif len(strs) > 1:
        prefix = ""
        s1 = sorted(strs, key=lambda x: len(x))[0]
        for i in range(len(s1)):
            for s in sorted(strs, key=lambda x: len(x))[1:]:
                if s1[i] == s[i]:
                    pass
                else:
                    return prefix
            prefix += s1[i]
    else:
        return ""

    return prefix
