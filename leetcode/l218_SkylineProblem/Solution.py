from typing import List
import heapq

class Solution:
    @staticmethod
    def get_skyline(buildings: List[List[int]]) -> List[List[int]]:
        ans = []
        max_heap = []  # -height, right
        i = 0
        n = len(buildings)
        while i < n or len(max_heap) != 0:
            # 樓有重疊: 新大樓的左邊座標，小於目前最高樓的右邊座標
            if len(max_heap) == 0 or i < n and \
               buildings[i][0] <= max_heap[0][1]:
                cur_right = buildings[i][0]
                # 不同大樓，左邊座標一樣的，放到heap裡面
                while i < n and cur_right == buildings[i][0]:
                    heapq.heappush(max_heap, (-buildings[i][2], buildings[i][1]))
                    i += 1
            else:
                cur_right = max_heap[0][1]
                # 把右邊座標在當前最高樓左側(被蓋住的點)的移出heap
                while len(max_heap) != 0 and cur_right >= max_heap[0][1]:
                    heapq.heappop(max_heap)

            cur_height = 0 if len(max_heap) == 0 else max_heap[0][0]
            if len(ans) == 0 or -cur_height != ans[-1][1]:
                ans.append([cur_right, -cur_height])
        return ans
