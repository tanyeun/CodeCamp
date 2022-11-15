from typing import List
import heapq

class Solution:
    @staticmethod
    def top_k_frequent(nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return nums

        book = {}
        for i in range(len(nums)):
            if nums[i] not in book:
                book[nums[i]] = 1
            else:
                book[nums[i]] += 1
        rank = []
        for key, value in book.items():
            heapq.heappush(rank, value)
            if len(rank) > k:
                heapq.heappop(rank)

        output = []
        threshold = heapq.heappop(rank)
        for key, value in book.items():
            if value >= threshold:
                output.append(key)
        return output
