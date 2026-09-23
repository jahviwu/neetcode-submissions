class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {} # Map value -> index

        for index, num in enumerate(nums):
            secNum = target - num

            if secNum in seen:
                return [seen[secNum], index]

            seen[num] = index

        return []
