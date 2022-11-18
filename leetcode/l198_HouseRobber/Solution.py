from typing import List


# dp[i] = max( dp[i-1], dp[i-2]+nums[i-1] )
#               不搶  vs     搶
# T: O(N)
# S: O(1)
class Solution:
    @staticmethod
    def rob(nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        first = nums[0]
        second = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            curr = max(second, first + nums[i])
            first = second
            second = curr
        return curr