class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','A','e','E','i','I','o','O','u','U']
        li = list(s)
        l = 0
        r = len(s) - 1

        while l < r:
            
            while l<r and li[l] not in vowels:
                l+=1
             
            while l<r and li[r] not in vowels:
                r-=1

            if l<r :
                li[l] , li[r] = li[r] , li[l]
            
            l+=1
            r-=1

        return "".join(li)

            