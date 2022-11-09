from typing import List


class Solution:
    @staticmethod
    def two_sum(numbers: List[int], target: int) -> List[int]:
        left = 1
        right = len(numbers)

        while left < right:
            res = numbers[left-1] + numbers[right-1]
            if res == target:
                return [left, right]
            elif res < target:
                left += 1
            else:
                right -= 1
