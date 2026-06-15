class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # result = ""
        # for i in range(len(word1)):
        #     result += word1[i]
        #     for j in range(len(word2)):
        #         result += word2[j]
        #         j+=1
        #         break
                
        
        # if word1:
        #     result += word1
        # else:
        #     result += word2

        # return "".join(result)

        l = 0
        r = 0
        result = ""
        w1,w2 = len(word1), len(word2)

        while l<w1 and r<w2:
            result += word1[l]
            result += word2[r]
            l+=1
            r+=1
        if l < w1:
            result += word1[l:]
        
        if r < w2:
            result += word2[r:]

        return result