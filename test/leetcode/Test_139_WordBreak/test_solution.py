from leetcode.l139_WordBreak.Solution import Solution


def test_case1():
    s = "leetcode"
    wordDict = ["leet","code"]
    output = Solution.word_break(s, wordDict)
    assert output is True


def test_case2():
    s = "applepenapple"
    wordDict = ["apple","pen"]
    output = Solution.word_break(s, wordDict)
    assert output is True


def test_case3():
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    output = Solution.word_break(s, wordDict)
    assert output is False

