from typing import List


# this solution is too slow
class Solution:
    @staticmethod
    def exist(board: List[List[str]], word: str) -> bool:
        def get_words(board, word, i, j, visited, pos=0):
            if pos == len(word):
                return True

            if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or  \
                    visited.get((i, j)) or word[pos] != board[i][j]:
                return False

            visited[(i, j)] = True
            res = get_words(board, word, i, j + 1, visited, pos + 1) \
                  or get_words(board, word, i, j - 1, visited, pos + 1) \
                  or get_words(board, word, i + 1, j, visited, pos + 1) \
                  or get_words(board, word, i - 1, j, visited, pos + 1)
            visited[(i, j)] = False

            return res

        visited = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if get_words(board, word, i, j, visited):
                    return True

        return False
