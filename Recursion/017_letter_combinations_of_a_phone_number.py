class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitsMap = {"2": "abc",
                     "3": "def",
                     "4": "ghi",
                     "5": "jkl",
                     "6": "mno",
                     "7": "pqrs",
                     "8": "tuv",
                     "9": "wxyz"}

        def backtrack(i, current_str):
            if len(current_str) == len(digits):
                res.append(current_str)
                return

            for c in digitsMap[digits[i]]:
                backtrack(i + 1, current_str + c)

        if digits:
            backtrack(0, "")

        return res
