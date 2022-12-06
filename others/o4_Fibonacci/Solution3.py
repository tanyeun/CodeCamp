class Solution:
    @staticmethod
    def fib(n):
        a = 1
        b = 1
        for i in range(2, n):
            a, b = b, a+b
        return b

    @staticmethod
    def fib_seq(n):
        a = 1
        b = 1
        seq = [0, a, b]
        for i in range(2, n):
            a, b = b, a+b
            seq.append(b)
        return seq

