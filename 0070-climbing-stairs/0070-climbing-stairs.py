class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n is 1 :
            return 1
        if n is 2 :
            return 2  #edge cases

        prev_one_step = 2 #a
        prev_two_step = 1  #b
        #bcoz 1,2 steps already given, Hence starts from step 3
        for i in range(3,n+1): 
            steps = prev_one_step + prev_two_step #<- C   #a+b
            prev_two_step = prev_one_step     #b = a
            prev_one_step = steps #a = c

        return prev_one_step
