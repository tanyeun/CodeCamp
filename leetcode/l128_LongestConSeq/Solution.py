from typing import List


# T: O(N)
# S: O(N)
class Solution:
    @staticmethod
    def longest_consecutive(nums: List[int]) -> int:
        num_set = set()
        for n in nums:
            num_set.add(n)

        max_length = 0
        for n in num_set:
            if n - 1 not in num_set:
                cur_num = n
                cur_length = 1
                while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_length += 1
                max_length = max(max_length, cur_length)

        return max_length