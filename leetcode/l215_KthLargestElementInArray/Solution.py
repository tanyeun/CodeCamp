import heapq
from typing import List
"""
 kth largest is equivalent to the min element 
 in the min heap with kth element
 
 T: O(NlogK)
 S: O(K)
 
 heapq is a binary heap, a heapq with K elements.
 push/pop operation takes O(logK)
 
 https://www.geeksforgeeks.org/binary-heap/
"""


class Solution:
    @staticmethod
    def find_kth_largest(nums: List[int], k: int) -> int:
        queue = []
        for i in range(len(nums)):
            heapq.heappush(queue, nums[i])
            if len(queue) > k:
                heapq.heappop(queue)
        return heapq.heappop(queue)

    @staticmethod
    def find_kth_minimum(nums: List[int], k: int) -> int:
        queue = []
        for i in range(len(nums)):
            heapq.heappush(queue, nums[i]*(-1))
            if len(queue) > k:
                heapq.heappop(queue)
        return heapq.heappop(queue) * (-1)