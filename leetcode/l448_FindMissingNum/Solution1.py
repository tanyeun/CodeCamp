from typing import List


# 利用原數組的index來記錄有沒有出現過
# 如果有出現過，就把值變成負數
# 如此可以省掉O(N)space, compared to Solution
class Solution:
    @staticmethod
    def find_disappeared_numbers(nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            new_index = abs(nums[i]) - 1
            if nums[new_index] > 0:
                nums[new_index] *= -1
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                res.append(i)
        return res