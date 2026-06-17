from collections import Counter
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        s = []
        left = 0
        right = 0


        while left < n:
            current_character = chars[left]
            count = 0

            while left < n and chars[left] == current_character:
                left += 1
                count += 1

            chars[right] = current_character
            right += 1

            if count > 1:
                for digit in str(count):
                    chars[right] = digit
                    right += 1
                    
        return right
            
        
        return 
