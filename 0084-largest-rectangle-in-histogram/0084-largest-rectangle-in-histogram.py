class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        stack = []
        heights.append(0)
        
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                current_height = heights[stack.pop()]

                width = i if not stack else i - stack[-1] - 1
                
                max_area = max(max_area, current_height * width)
            
            stack.append(i)

        heights.pop() 
        return max_area