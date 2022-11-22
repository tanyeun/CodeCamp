from typing import List


# index magic
class Solution:
    @staticmethod
    def span(nums: List) -> List:
        index1 = []
        out = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] == 1:
                index1.append(i)

        for i in range(len(index1)):
            if i+1 < len(index1):
                out[index1[i]] = index1[i+1] - index1[i]
            if i+1 == len(index1) and i < len(nums):
                out[index1[i]] = len(nums) - index1[i]

        return out