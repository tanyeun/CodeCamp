class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        dictionary = {}
        substr = ""
        max_len = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in dictionary:
                    dictionary[s[j]] = 1
                    substr += s[j]
                else:
                    break
            if len(substr) > max_len:
                max_len = len(substr)
            dictionary = {}
            substr = ""

        return max_len
