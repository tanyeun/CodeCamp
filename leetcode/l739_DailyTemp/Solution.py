from typing import List


# 單調棧 monotonic stack
# T: O(N)
# S: O(N)
class Solution:
    @staticmethod
    def daily_temperatures(temperatures: List[int]) -> List[int]:
        stack = []
        wait = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while len(stack) != 0:
                index_min_temp = stack[-1]
                if temperatures[i] <= temperatures[index_min_temp]:
                    break
                stack.pop()
                wait[index_min_temp] = i-index_min_temp
            stack.append(i)
        return wait