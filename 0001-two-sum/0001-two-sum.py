class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        read = {}
        for i , num in enumerate(nums):
            sums = target - num 
            if sums in read:
                return [read[sums],i]
            read[num] = i
        return [ ] 