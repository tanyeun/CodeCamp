

class Solution:
    @staticmethod
    def min_window(s: str, t: str) -> str:
        hashmap = [0]*128  # 128 ascii values
        in_t = [False]*128

        # ord('A') = 65
        # ord('a') = 97
        for i in range(0, len(t)):
            hashmap[ord(t[i])] += 1
            in_t[ord(t[i])] = True

        cnt = 0
        left = 0
        min_l = 0
        min_size = len(s) + 1
        for right in range(0, len(s)):
            if in_t[ord(s[right])]:
                hashmap[ord(s[right])] -= 1
                if hashmap[ord(s[right])] >= 0:
                    cnt += 1
                while cnt == len(t):
                    if right-left+1 < min_size:
                        min_size = right-left+1
                        min_l = left
                    if in_t[ord(s[left])]:
                        hashmap[ord(s[left])] += 1
                        if hashmap[ord(s[left])] > 0:
                            cnt -= 1
                    left += 1
        return "" if min_size > len(s) else s[min_l:min_l+min_size]
