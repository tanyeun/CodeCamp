from typing import List


# intuitive solution, too slow when both len(nums) and k are large
class Solution:
    @staticmethod
    def max_sliding_window(nums: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(nums)-k+1):
            compare = []
            for j in range(k):
                compare.append(nums[i+j])
            ans.append(max(compare))
        return ans