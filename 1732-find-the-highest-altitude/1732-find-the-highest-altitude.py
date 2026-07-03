class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        cur_att = 0
        high_att = 0

        for g in gain:
            cur_att += g
            high_att = max(high_att, cur_att)

        return high_att