from typing import List


class Solution:
    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # pointers to the end of the list
        ptr = m + n - 1
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[ptr] = nums1[m-1]
                m -= 1
            else:
                nums1[ptr] = nums2[n-1]
                n -= 1
            ptr -= 1

        # for the case nums2 still have elements
        while n > 0:
            nums1[ptr] = nums2[n-1]
            n -= 1
            ptr -= 1