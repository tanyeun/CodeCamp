from leetcode.l126_WordLadder2.Solution import Solution


def test_case1():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    output = Solution.find_ladders(beginWord, endWord, wordList)
    assert output == []


def test_case2():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    output = Solution.find_ladders(beginWord, endWord, wordList)
    assert sorted(output) == sorted([["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]])
