class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged_result = []
        i = 0
        j = 0

        while i < len(word1) and j < len(word2):
            merged_result.append(word1[i])
            merged_result.append(word2[j])
            i+=1
            j+=1
#remaining values to be appended
        if i < len(word1):
            merged_result.append(word1[i:])
        
        if j < len(word2):
            merged_result.append(word2[j:])

        return ''.join(merged_result)
