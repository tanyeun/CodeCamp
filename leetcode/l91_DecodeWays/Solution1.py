

class Solution:
    @staticmethod
    def num_decodings(s: str) -> int:
        last, now = 1, int('1' <= s[0] <= "9")

        for i in range(1, len(s)):
            c = s[i]
            curr = 0
            if '1' <= c <= '9':
                curr += now
            if '10' <= s[i - 1: i + 1] <= '26':
                curr += last
            last = now
            now = curr

        return now
