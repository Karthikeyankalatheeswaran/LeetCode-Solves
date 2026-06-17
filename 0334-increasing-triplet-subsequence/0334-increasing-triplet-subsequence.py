class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # n = len(nums)
        # left = 0

        # for right in range(2,n):
        #     if nums[left] < nums[left + 1] < nums[right]:
        #         return True
        #     left +=1
        #     right +=1
        # return False

        #AI ANSWER

        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num      # Smallest element found so far
            elif num <= second:
                second = num     # Mid element found (greater than first)
            else:
                return True      # Large element found (greater than first and second)
                
        return False
        