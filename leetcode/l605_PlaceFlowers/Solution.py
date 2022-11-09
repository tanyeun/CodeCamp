from typing import List


class Solution:
    @staticmethod
    def can_place_flowers(flowerbed: List[int], n: int) -> bool:
        max_flower = 0
        size = len(flowerbed)
        flowerbed.append(0)

        # edge case
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            max_flower += 1
            flowerbed[0] = 1

        for i in range(1, size):
            if flowerbed[i] == 0:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    max_flower += 1
                    flowerbed[i] = 1

        if n <= max_flower:
            return True
        else:
            return False
