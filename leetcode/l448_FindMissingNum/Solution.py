from typing import List


class Solution:
    @staticmethod
    def find_disappeared_numbers(nums: List[int]) -> List[int]:
        n = len(nums)

        lookup = [0]*n

        for i in range(n):
            lookup[nums[i]-1] = 1

        out = []
        for i in range(n):
            if lookup[i] == 0:
                out.append(i+1)

        return out