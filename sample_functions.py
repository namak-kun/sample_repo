def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

class t:
    def fib(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 1
        return self.fib(n-1) + self.fib(n-2)