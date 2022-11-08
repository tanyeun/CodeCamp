from typing import List


# this solution is too slow based on Leetcode data on 11/8/2022
class Solution:
    @staticmethod
    def candy(ratings: List[int]) -> int:
        size = len(ratings)
        if size <= 1:
            return size

        result = [1] * size
        for i in range(0, size-1, 1):
            if ratings[i+1] > ratings[i]:
                result[i+1] = result[i] + 1

        for i in range(size-1, 0, -1):
            if ratings[i] < ratings[i-1]:
                result[i-1] = max(result[i-1], result[i]+1)

        return sum(result)