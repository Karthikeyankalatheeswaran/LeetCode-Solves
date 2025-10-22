class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counts_map = {}

        for x in arr:
            counts_map[x] = counts_map.get(x, 0) + 1

        seen_counts = set()

        for count in counts_map.values():
            if count in seen_counts:
                return False

            seen_counts.add(count)
        
        return True