class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        close_number = nums[0]
        for i in nums[1:]:
            if abs(i) < abs(close_number):
                close_number = i
            elif abs(i) == abs(close_number):
                if i > close_number:
                    close_number = i
        return close_number