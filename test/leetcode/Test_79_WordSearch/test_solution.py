from leetcode.l79_WordSearch.Solution import Solution


def test_case1():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    output = Solution.exist(board, word)
    assert output is True


def test_case2():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    output = Solution.exist(board, word)
    assert output is True


def test_case3():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    output = Solution.exist(board, word)
    assert output is False