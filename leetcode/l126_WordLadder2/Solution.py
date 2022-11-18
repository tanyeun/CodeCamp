from typing import List
from collections import defaultdict


# this solution is too slow
class Solution:
    @staticmethod
    def find_ladders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        graph = defaultdict(set)
        for word in wordList + [beginWord]:
            for i in range(len(word)):
                graph[word[:i] + '_' + word[i + 1:]].add(word)
        wordList = set(wordList)

        queue = [[beginWord]]
        flag = False
        while queue:
            new_queue = []
            to_remove = set()
            for path in queue:
                for i in range(len(path[-1])):
                    for new_word in graph[path[-1][:i] + '_' + path[-1][i + 1:]] & wordList:
                        new_queue.append(path + [new_word])
                        to_remove.add(new_word)
                        if new_word == endWord: flag = True
            if flag: return [p for p in new_queue if p[-1] == endWord]
            queue = new_queue[:]
            wordList -= to_remove
        return []
