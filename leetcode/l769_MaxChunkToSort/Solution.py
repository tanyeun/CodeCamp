from typing import List


# 當目前最大值 == 現在位置的時候，可以增加一個分割
# 因為，數組是0~n不重複的值
class Solution:
    @staticmethod
    def max_chunks_to_sorted(arr: List[int]) -> int:
        cur_max = 0
        count = 0
        for i in range(len(arr)):
            cur_max = max(cur_max, arr[i])
            if cur_max == i:
                count += 1
        return count
