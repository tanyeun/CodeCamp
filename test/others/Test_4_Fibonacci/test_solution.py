from others.o4_Fibonacci.Solution3 import Solution
import timeit

def test_case1():
    n = 10
    output = Solution.fib(n)
    assert output == 55


def test_case2():
    n = 20
    output = Solution.fib(n)
    assert output == 6765


# Sol: 23.292545500036795
# Sol1:0.001648699981160462
# Sol2:0.0008445000275969505
# Sol3:8.760002674534917e-05
def test_case3():
    n = 30
    t = timeit.timeit('Solution.fib(30)', number=100, globals=globals())
    print("execution: ", t)
    output = Solution.fib(n)
    assert output == 832040


def test_case4():
    n = 8
    output = Solution.fib(n)
    seq = Solution.fib_seq(n)
    print(seq)
    print(sum(seq))
    assert output == 21


# Sol3: 0.0003264000406488776 / 10000
# Sol2: 0.0003208999987691641 / 10000
# Sol1: 0.00031999999191612005  / 10000 iterations
# Sol:  0.0007475999882444739 / 10000
def test_time():
    iterations = 10000
    t1 = timeit.timeit('test_case1', number=iterations, globals=globals())
    t2 = timeit.timeit('test_case2', number=iterations, globals=globals())
    t3 = timeit.timeit('test_case3', number=iterations, globals=globals())
    print("execution: ", t1+t2+t3)