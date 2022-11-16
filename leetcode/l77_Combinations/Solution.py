from typing import List


class Solution:
    @staticmethod
    def combine(n: int, k: int) -> List[List[int]]:
        def backtrack(first=1, curr=[]):
            # if the combination is done
            if len(curr) == k:
                # curr[:] makes a copy of curr from index 0 to end
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                # if you put first+1 instead of i+1
                # you will get permutation instead of combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        backtrack()
        return output
