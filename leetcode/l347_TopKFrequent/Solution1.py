from typing import List

# this solution is faster
class Solution:
    # bucket sort solution
    @staticmethod
    def top_k_frequent(nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return nums

        book = {}
        max_count = 0
        for i in range(len(nums)):
            if nums[i] not in book:
                book[nums[i]] = 1
            else:
                book[nums[i]] += 1
            if max_count < book[nums[i]]:
                max_count = book[nums[i]]

        # the index of the bucket is the frequency
        # index 3 has [1,2] means element 1, 2 appears 3 times
        bucket = [[] for i in range(max_count+1)]
        for key, value in book.items():
            bucket[value].append(key)

        output = []
        index = max_count
        while index >= 0 and len(output) < k:
            for v in bucket[index]:
                output.append(v)
                if len(output) == k:
                    break
            index -= 1
        return output
