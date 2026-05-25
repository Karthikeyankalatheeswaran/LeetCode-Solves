class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l = 0
        r = n - 1
        max_res = 0

        while l < r:
            w = r - l
            h = min(height[l], height[r])
            area = h * w
            max_res = max(max_res, area)

            if height[l] < height[r]:
                l +=1

            else:
                r-=1

        return max_res