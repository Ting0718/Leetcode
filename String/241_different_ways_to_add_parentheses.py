class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if not expression:
            return []

        res = []
        for i in range(len(expression)):
            c = expression[i]
            if c == "-" or c == "+" or c == "*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])

                for l in left:
                    for r in right:
                        if c == "+":
                            res.append(l+r)
                        if c == "-":
                            res.append(l-r)
                        if c == "*":
                            res.append(l*r)

        if len(res) == 0:
            res.append(int(expression))

        return res
