class Solution:
    # f(n) = max(f(i-1), f(i-2)+nums[i])
    @staticmethod
    def flowerbox(nums):
        a = 0
        b = 0
        for n in nums:
            a, b = b, max(a+n, b)
        return b
