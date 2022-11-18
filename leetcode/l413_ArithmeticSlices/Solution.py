from typing import List


class Solution:
    @staticmethod
    def number_of_arithmetic_slices(nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        dp = [0]*n
        for i in range(2, n):
            if nums[i-1] - nums[i] == nums[i-2] - nums[i-1]:
                dp[i] = dp[i-1] + 1

        return sum(dp)
