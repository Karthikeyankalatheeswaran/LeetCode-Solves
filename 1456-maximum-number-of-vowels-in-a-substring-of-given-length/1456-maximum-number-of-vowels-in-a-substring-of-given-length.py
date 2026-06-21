class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        left  = 0
        count , result = 0 , 0
        vowels = {"a",'e','i','o','u'}

        for right in range(n):
            count += 1 if s[right] in vowels else 0 

            if right - left + 1 > k:
                count -=1 if s[left] in vowels else 0
                left+=1
            result = max(result,count)

        return result




