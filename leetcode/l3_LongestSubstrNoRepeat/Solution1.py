class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        max_len = 0
        # dictionary stores the current index of a character
        dictionary = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(len(s)):
            if s[j] in dictionary:
                i = max(dictionary[s[j]], i)

            # j-i+1: the distance between position i and j
            # j+1: the distance from j to position 0
            # dictionary: char -> distance to position 0
            max_len = max(max_len, j - i + 1)
            dictionary[s[j]] = j + 1

        return max_len