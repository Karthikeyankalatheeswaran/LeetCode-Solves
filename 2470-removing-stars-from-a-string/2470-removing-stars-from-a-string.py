class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for character in s:
            if character != "*":
                stack.append(character)
            else:
                if stack:
                    stack.pop()

        return "".join(stack)