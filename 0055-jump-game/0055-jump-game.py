class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        
        for i, jump in enumerate(nums):
            # If we can't reach this index, we can't go further
            if i > max_reach:
                return False
            
            # Update the furthest we can reach
            max_reach = max(max_reach, i + jump)
            
            # Optimization: Early exit if we can already reach the end
            if max_reach >= len(nums) - 1:
                return True
                
        return True