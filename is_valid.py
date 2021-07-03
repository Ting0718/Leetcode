class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i in d.values():
                stack.append(i)
            else:
                if len(stack) != 0 and d[i] == stack.pop():
                    pass
                else:
                    return False
        return len(stack) == 0
