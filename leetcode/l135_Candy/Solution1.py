from typing import List
import math

"""
ratings如果是完全遞減的數列，stack裡面就是紀錄每個人發的糖果數量
Case 4:
  [1,1,0,-1,-2] 掃過一遍之後
  最後一個element人工設成inf，所以開始遞增
  用len(stack) > 1去檢查，發現有遞減數列
  於是用max(0, 1 - stack[-1])去找實際發的糖果數量
  因為不可能發 [0,-1,-2]，糖果最少要發一個
  所以把delta加上去，stack變成
  [1,4,3,2,1]
  又，stack[0]一定還是要比stack[1]多一個(第一個人比第二個人多1，因為遞減的緣故)
  所以在針對第一個element處理成
  [5,4,3,2,1]
Case 1:
  在[1,0]結束的時候，就開始進入遞增
  這時候stack是
  [1,1], delta是零(因為沒有出現負數)，所以不變
  最後在處理第一個element變成
  [2,1]
  2+1 = 3是遞減數列部分發出的糖果數量
  開始遞增的rating是2
  把遞減的stack清空，用[max(1, stack[-1]) + 1][2]取代
"""

# time = 0.04
class Solution:
    @staticmethod
    def helper(ans, stack):
        # 檢查前段數列有沒有遞減
        if len(stack) > 1:
            # stack[-1] is to top of stack
            # stack[0] is the first element in the stack
            delta = max(0, 1 - stack[-1])
            # make sure the lowest gets 1 candy
            for j in range(1, len(stack)):
                stack[j] += delta
            # handle the first element separately for consistency
            if stack[0] <= stack[1]:
                stack[0] = stack[1] + 1
        ans += sum(stack)
        return ans

    @staticmethod
    def candy(ratings: List[int]) -> int:
        ans = 0

        ratings.append(math.inf)
        n = len(ratings)

        stack = [1]
        for i in range(1, n):
            # 數列遞增
            if ratings[i] > ratings[i - 1]:
                ans = Solution.helper(ans, stack)
                # make sure it is consistent to the left
                stack = [max(1, stack[-1]) + 1]
            # 不增不減
            elif ratings[i] == ratings[i - 1]:
                ans = Solution.helper(ans, stack)
                # here always give 1 candy
                stack = [1]
            # 遞減
            else:
                # this is to make sure we don't give more than necessary
                if len(stack) == 1:
                    stack.append(1)
                else:
                    stack.append(stack[-1] - 1)
        return ans
