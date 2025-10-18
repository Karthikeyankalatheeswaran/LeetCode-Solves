class Solution(object):
    def findDifference(self, nums1, nums2):
        arr1 = set(nums1)
        arr2 = set(nums2)
        
        match1 = []

        for num in arr1:
            if num not in arr2:
                match1.append(num)
        
        match2 = []

        for num in arr2:
            if num not in arr1:
                match2.append(num)

        return [match1,match2]


