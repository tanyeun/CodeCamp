from typing import List
from collections import deque

class Solution:
    @staticmethod
    def shortest_bridge(grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # 记录island 1的所有沿海点
        coastal = set()
        x, y = 0, 0
        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    x, y = i, j
                    found = True
                    break
            if found:
                break

        q = deque([(x, y)])
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if grid[nx][ny] == 0:
                        coastal.add((x, y))
                    elif grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx, ny))
        # 从island 1的所有沿海点出发宽搜找island2
        q = deque(coastal)
        dist = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 2
                            q.append((nx, ny))
                        elif grid[nx][ny] == 1:
                            return dist

            dist += 1

