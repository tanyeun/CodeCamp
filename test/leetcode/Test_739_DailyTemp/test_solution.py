from leetcode.l739_DailyTemp.Solution import Solution


def test_case1():
    temperatures = [73,74,75,71,69,72,76,73]
    output = Solution.daily_temperatures(temperatures)
    assert output == [1,1,4,2,1,1,0,0]


def test_case2():
    temperatures = [30,40,50,60]
    output = Solution.daily_temperatures(temperatures)
    assert output == [1,1,1,0]


def test_case3():
    temperatures = [30,60,90]
    output = Solution.daily_temperatures(temperatures)
    assert output == [1,1,0]
