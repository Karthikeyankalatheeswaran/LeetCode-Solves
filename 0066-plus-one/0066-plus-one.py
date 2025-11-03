class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        single_value = int("".join(map(str, digits)))

        result = single_value + 1

        result_string = str(result)
        result_array = [int(digit) for digit in result_string]

        return result_array