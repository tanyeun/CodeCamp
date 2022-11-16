from typing import List

# 440ms, 15.6MB
class Solution:
    @staticmethod
    def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
        # Time: O(mn) and Space: O(mn)

        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        # current location, set of already visited tiles, the value
        # of the tile where we are calling the dfs function
        def dfs(r, c, visit, prev_height):

            # we will check if the index[r, c] is not already visited,
            # row and column is inbounds and
            # the current tile should be lower than from we are coming
            # from, it's the condition for waterflow mentioned
            # if any one of these conditions fails exit the dfs by
            # returning to from we came from
            if (r, c) in visit or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prev_height:
                return

            visit.add((r, c))
            # mark the tile visited(pac or atl depending on what
            # is passed from the dfs function) when the if conditions true

            dfs(r + 1, c, visit, heights[r][c])  # we will next visit the tile down from the current one
            dfs(r - 1, c, visit, heights[r][c])  # up
            dfs(r, c + 1, visit, heights[r][c])  # right
            dfs(r, c - 1, visit, heights[r][c])  # left

        # we will traverse the first & last row by fixing the r and moving c
        for c in range(cols):
            # first row is just next to pacific
            dfs(0, c, pac, heights[0][c])
            # last row is just next to atlantic
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        # we will traverse the first & last column by fixing the c and moving r
        for r in range(rows):
            # first column is just next to pacific
            dfs(r, 0, pac, heights[r][0])
            # last column is just next to atlantic
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        # returns the list which contains the same [i, j] in both the sets
        return list(pac.intersection(atl))
