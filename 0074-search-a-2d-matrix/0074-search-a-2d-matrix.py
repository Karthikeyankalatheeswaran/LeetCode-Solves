class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        rows , cols = len(matrix), len(matrix[0])
        low, high = 0,(rows * cols) - 1

        while low<=high:
            mid = (low + high)//2
            r,c = divmod(mid,cols)
            num = matrix[r][c]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False