'''recursion'''
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

'''dp'''
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        v1, v2 = 0, 1
        x = 2
        while x <= n:
            x += 1
            v1, v2 = v2, v1 + v2

        return v2
