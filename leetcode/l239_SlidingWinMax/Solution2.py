from typing import List
from collections import deque


class Solution:
    @staticmethod
    # Solution2跟1的演算法基本一樣，但是不知道為啥
    def max_sliding_window(nums: List[int], k: int) -> List[int]:
        answer = []
        window = deque()
        window_size = k
        if len(nums) == 0:
            return answer

        # Find maximum in first window
        for i in range(window_size):
            # For every element, remove the previous smaller
            # elements from window
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            # Add current element at the back of queue
            window.append(i)
        # append the largest element in the window to the result
        answer.append(nums[window[0]])
        for i in range(window_size, len(nums)):
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            if window and window[0] <= (i - window_size):
                window.popleft()
            window.append(i)
            answer.append(nums[window[0]])
        return answer
