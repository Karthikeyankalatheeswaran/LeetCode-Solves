class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {}
        i = 0 
        max_length = 0
        
        for j, char in enumerate(s):
            if char in last_seen and last_seen[char] >= i:
                i = last_seen[char] + 1

            last_seen[char] = j

            max_length = max(max_length, j - i + 1)
            
        return max_length