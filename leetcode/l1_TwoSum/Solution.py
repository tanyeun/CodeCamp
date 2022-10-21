from typing import List


class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        dictionary = {}
        """
          number -> index
        """
        for i in range(len(nums)):
            candidate = target - nums[i]
            if candidate in dictionary:
                return [i, dictionary[candidate]]
            else:
                dictionary[nums[i]] = i
