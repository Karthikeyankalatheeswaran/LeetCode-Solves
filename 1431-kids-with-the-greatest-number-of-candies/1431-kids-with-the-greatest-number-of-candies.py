class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []*len(candies)
        max_val = max(candies)

        for i in range(len(candies)):
            summ = candies[i] + extraCandies
            if summ >= max_val:
                result.append(True)
            else:
                result.append(False)
        
        return result
            

