class Solution:
    def fib(self, n: int) -> int:
        d = {0:0,1:1}
        def fibonacci(n,d):
            if n in d:
                return d[n]
            else:
                d[n] = fibonacci(n-1,d) + fibonacci(n-2,d)
                return d[n]
        return fibonacci(n,d)