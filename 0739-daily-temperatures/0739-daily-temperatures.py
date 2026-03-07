class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        stack = [] 

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                stackInd = stack.pop()    
                res[stackInd] = i - stackInd 

            stack.append(i)
            
        return res
