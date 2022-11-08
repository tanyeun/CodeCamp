from typing import List

class Solution:
    @staticmethod
    def find_content_children(g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        greed = 0
        cookie = 0

        while greed < len(g) and cookie < len(s):
            if g[greed] <= s[cookie]:
                greed = greed + 1
            cookie = cookie + 1

        return greed