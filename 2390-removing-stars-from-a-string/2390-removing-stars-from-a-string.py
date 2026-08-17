class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = []

        for character in s:
            if character != "*":
                stk.append(character)
            else:
                if stk:
                    stk.pop()

        return "".join(stk)