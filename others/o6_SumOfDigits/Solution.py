

class Solution:
    @staticmethod
    def digital_root(n):
        def digit_sum(m):
            ans = 0
            while m:
                ans += (m % 10)
                m //= 10
            return ans

        output = digit_sum(n)
        while output >= 10:
            output = digit_sum(output)

        return output
