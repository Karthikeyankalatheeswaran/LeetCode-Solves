class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x % 10 == 0 and x != 0:
            return False

        original_x = x
        reversed_number = 0
        
        while original_x > 0:
            digit = original_x % 10
            reversed_number = reversed_number * 10 + digit
            original_x //= 10
            
        return x == reversed_number