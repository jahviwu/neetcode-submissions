class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            startIndex = i
            while stack and stack[-1][1] > h: # If Stack not empty and the height of the last added index is greater than the current height
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                startIndex = index # Extend start index to the index we just popped 
            stack.append((startIndex, h))

        # For the remaining uncomputed areas
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea