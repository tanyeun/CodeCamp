from typing import List
# still need to figure this out
# how to calculate the duplicate

class Solution:
    @staticmethod
    def max_points(points: List[List[int]]) -> int:
        if not points: return 0
        L = len(points)
        if L < 2: return 1
        result = 0
        for i in range(L):
            myMap, verticle, duplicate = {}, 0, 0
            for j in range(i + 1, L):
                a = points[i]
                b = points[j]
                if a[0] == b[0]:
                    if a[1] != b[1]:
                        verticle += 1
                    else:
                        duplicate += 1
                else:
                    slope = float(b[1] - a[1]) / float(b[0] - a[0])
                    myMap[slope] = myMap.setdefault(slope, 0) + 1

            try:
                slopeMax = max(myMap.values())
            except:
                slopeMax = 0
            maxPointOnLine = max(slopeMax, verticle) + duplicate
            if maxPointOnLine > result: result = maxPointOnLine

        return result + 1
