class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures) # list of 0s with the size of temp

        for i, t in enumerate(temperatures):
            # While Stack is not empty AND current temp is greater than the last added i,t pair "[-1]"
            #"[1]" is the second value of that pair which represents the temp 
            # [1] can also be [0] with it being t,i as long as we are consistent when calling it
            while stack and t > stack[-1][1]:  
                stackInd, stackT = stack.pop() # Consistent with our logic (i, t)

                res[stackInd] = i - stackInd # warmer day index - current day index = days inbetween
            stack.append([i, t]) 
        return res