from typing import List
from collections import deque


class Solution:
    # 保持dq双端队列嚴格遞減
    # dq[0] > dq[1] > dq[2] > ... > dq[-1]
    # 真神奇，loop裡面先pop在popleft比先popleft快很多
    @staticmethod
    def max_sliding_window(nums: List[int], k: int) -> List[int]:
        ans = []
        dq = deque()

        if len(nums) == 0:
            return ans

        for i in range(len(nums)):
            # 新的值比dq內最小值大，把最小值移除
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            # 當最大值的位置已經不在window範圍內時移除
            if dq and dq[0] <= i-k:
                dq.popleft()
            # 確保新值加入時，滿足dq是嚴格遞減
            dq.append(i)
            if i >= k-1:  # 滿足window長度之後，每一輪都會把dq最大值新增
                ans.append(nums[dq[0]])

        return ans