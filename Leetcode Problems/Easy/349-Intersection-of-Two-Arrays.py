'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        output = []
        
        if len(nums1) > len(nums2):
            for i in nums2:
                if i in nums1 and i not in output:
                    output.append(i)
        else:
            for i in nums1:
                if i in nums2 and i not in output:
                    output.append(i)
        return output
