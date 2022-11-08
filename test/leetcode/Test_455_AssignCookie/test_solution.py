from leetcode.l455_AssignCookie.Solution import Solution


def test_case1():
    g = [1, 2, 3]
    s = [1, 1]
    output = Solution.find_content_children(g, s)
    assert output == 1

def test_case2():
    g = [1, 2]
    s = [1, 2, 3]
    output = Solution.find_content_children(g, s)
    assert output == 2