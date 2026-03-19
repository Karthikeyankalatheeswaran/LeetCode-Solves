from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        
        target_count = Counter(t)
        window_count = {}

        have, need = 0, len(target_count)
        res, res_len = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1

            if char in target_count and window_count[char] == target_count[char]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                left_char = s[l]
                window_count[left_char] -= 1
                if left_char in target_count and window_count[left_char] < target_count[left_char]:
                    have -= 1
                l += 1
                
        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""
