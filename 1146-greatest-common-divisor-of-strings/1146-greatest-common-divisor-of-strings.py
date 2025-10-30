class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""

        len1 = len(str1)
        len2 = len(str2)

        a = len1
        b = len2
        
        while b:
            a, b = b, a % b
        gcd_length = a
        return str1[:gcd_length]