class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(b) < len(a):
            a, b = b, a # first array should be shorter 

        l, r = 0, len(a) - 1
        while True:
            aPointer = (l + r) // 2
            bPointer = half - aPointer - 2 # subtract 2 bc indexes start at 0 and apointer and bpointer have 2 0's

            aLeft = a[aPointer] if aPointer >= 0 else float("-infinity")
            aRight = a[aPointer + 1] if (aPointer + 1) < len(a) else float("infinity")
            bLeft = b[bPointer] if bPointer >= 0 else float("-infinity")
            bRight = b[bPointer + 1] if (bPointer + 1) < len(b) else float("infinity")

            if aLeft <= bRight and bLeft <= aRight:
                # odd amount
                if total % 2:
                    return min(aRight, bRight)
                # even
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft > bRight:
                r = aPointer - 1
            else:
                l = aPointer + 1
        
