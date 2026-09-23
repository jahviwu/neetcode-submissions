class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # 1. Found the target
            if target == nums[mid]:
                return mid

            # 2. Check if the Left Half is sorted
            if nums[left] <= nums[mid]:
                # Is the target in the sorted left half?
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # 3. Right Half must be sorted
            else:
                # Is the target in the sorted right half?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1