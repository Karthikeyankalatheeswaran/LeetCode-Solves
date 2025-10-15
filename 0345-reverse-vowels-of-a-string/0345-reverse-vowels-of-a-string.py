class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        left = 0
        right = len(s_list) - 1

        while left < right:

            while left < right and s_list[left] not in VOWELS:
                left += 1
                
            while left < right and s_list[right] not in VOWELS:
                right -= 1
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                
                left += 1
                right -= 1
        return "".join(s_list)