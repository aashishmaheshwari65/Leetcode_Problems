class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        total_length = len(nums1) + len(nums2)
        array = []

        i = 0
        j = 0

    
        while i < len(nums1) and j < len(nums2):

            if nums1[i] <= nums2[j]:
                array.append(nums1[i])
                i += 1
            else:
                array.append(nums2[j])
                j += 1

    
        while i < len(nums1):
            array.append(nums1[i])
            i += 1

        while j < len(nums2):
            array.append(nums2[j])
            j += 1

        
        n = total_length // 2

        if total_length % 2 == 0:
            median = (array[n - 1] + array[n]) / 2
        else:
            median = array[n]

        return median
