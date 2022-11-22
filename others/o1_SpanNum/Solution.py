from typing import List


# 透過紀錄上一次1出現的時機，來記錄中間有幾個零
class Solution:
    @staticmethod
    def span(nums: List) -> List:
        last1 = -1
        zeros = 0
        out = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] == 1:
                if last1 != -1:
                    out[last1] = 1+zeros
                    zeros = 0
                    last1 = i
                else:
                    last1 = i
            else:
                if last1 != -1:
                    zeros += 1
        if last1 != -1:
            out[last1] = 1+zeros
        return out