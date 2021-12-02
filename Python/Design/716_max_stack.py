class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return None
        return self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def peekMax(self) -> int:
        if not self.stack:
            return None
        return max(self.stack)

    def popMax(self) -> int:
        maximum = self.peekMax()
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i] == maximum:
                n = self.stack[i]
                self.stack.pop(i)
                break
        return n