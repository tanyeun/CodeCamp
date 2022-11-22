from typing import List


# 倒過來做
class Solution:
    @staticmethod
    def span(nums: List) -> List:
        last1 = -1
        zeros = 0
        out = [0]*len(nums)
        for i in range(len(nums)-1, 0):
            if nums[i] == 1:
                out[i] = 1 + zeros
                zeros = 0
            else:
                zeros += 1

        return out