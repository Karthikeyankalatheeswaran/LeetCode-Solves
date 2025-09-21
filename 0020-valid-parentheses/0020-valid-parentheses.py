class Solution(object):
    def isValid(self, s):
        stack = []
        brackets = {")": "(",  "}": "{",  "]": "["}

        for char in s:
            if char in brackets:
                top = stack.pop() if stack else '0'

                if brackets[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack

        