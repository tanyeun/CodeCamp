from others.o5_FlowerBox.Solution import Solution
import timeit

def test_case1():
    nums=[3,10,3,1,2]
    output = Solution.flowerbox(nums)
    assert output == 12


# Sol: 23.292545500036795
def test_case3():
    t = timeit.timeit('Solution.flowerbox([9,10,9])', number=100, globals=globals())
    print("execution: ", t)
    nums=[9,10,9]
    output = Solution.flowerbox(nums)
    assert output == 18
