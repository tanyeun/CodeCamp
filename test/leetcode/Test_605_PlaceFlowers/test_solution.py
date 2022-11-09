from leetcode.l605_PlaceFlowers.Solution import Solution


def test_case1():
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    output = Solution.can_place_flowers(flowerbed, n)
    assert output is True


def test_case2():
    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    output = Solution.can_place_flowers(flowerbed, n)
    assert output is False


def test_case3():
    flowerbed = [0, 0, 1, 0, 1]
    n = 1
    output = Solution.can_place_flowers(flowerbed, n)
    assert output is True
