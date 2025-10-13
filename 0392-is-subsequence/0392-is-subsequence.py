class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0 
        j = 0

        s_len = len(s)
        t_len = len(t)

        if s_len == 0:
            return True

        while i < s_len and j < t_len:
            if s[i] == t[j]:
                i +=1
            j+=1

        return i == s_len
        