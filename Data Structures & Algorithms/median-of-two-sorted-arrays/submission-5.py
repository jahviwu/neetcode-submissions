class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(b) < len(a):
            a, b = b, a # first array should be shorter 

        l, r = 0, len(a) - 1
        while True:
            i = (l + r) // 2 # mid of i 
            j = half - i - 2 # subtract 2 bc indexes start at 0 and apointer and bpointer have 2 0's

            aLeft = a[i] if i >= 0 else float("-infinity")
            aRight = a[i + 1] if (i + 1) < len(a) else float("infinity")
            bLeft = b[j] if j >= 0 else float("-infinity")
            bRight = b[j + 1] if (j + 1) < len(b) else float("infinity")

            if aLeft <= bRight and bLeft <= aRight:
                # odd amount
                if total % 2:
                    return min(aRight, bRight)
                # even
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft > bRight:
                r = i - 1
            else:
                l = i + 1
        
