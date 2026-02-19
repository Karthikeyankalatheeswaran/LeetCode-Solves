class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_list = set()

        for num in nums:
            if num in num_list:
                return True
            else:
                num_list.add(num)
        return False