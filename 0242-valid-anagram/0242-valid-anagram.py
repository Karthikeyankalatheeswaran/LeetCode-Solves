from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!= len(t):
            return False

        s_an = Counter(s)
        t_an = Counter(t)

        return s_an == t_an