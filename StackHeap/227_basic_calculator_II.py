class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        operation = "+"
        stack = []

        for i in range(len(s)):
            if s[i].isnumeric():
                num = num*10 + int(s[i])

            if s[i] in "+-*/" or i == len(s) - 1:
                if operation == "+":
                    stack.append(num)
                elif operation == "-":
                    stack.append(-num)
                elif operation == "*":
                    r = stack.pop() * num
                    stack.append(r)
                elif operation == "/":
                    r = int(stack.pop() / num)
                    stack.append(r)

                operation = s[i]
                num = 0

        return sum(stack)
