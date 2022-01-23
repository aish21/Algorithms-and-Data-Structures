class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        final = m + n - 1
        first = m - 1
        second = n - 1
        
        while first >= 0 and second >= 0:
            if(nums1[first] > nums2[second]):
                nums1[final] = nums1[first]
                first -= 1
                final -= 1
            else:
                nums1[final] = nums2[second]
                second -= 1
                final -= 1
                
        if first < 0:  
            nums1[:final+1] = nums2[:second+1]
        else:
            nums1[:final+1] = nums1[:first+1]