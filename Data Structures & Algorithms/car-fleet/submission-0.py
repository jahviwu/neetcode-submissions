class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Sort in descending order because the position of the car closest to the target determines when the other cars become a fleet 
        # Ex. if C1 catches up to C2, they both slow down, but if we know C2 catches up to C3, C1 still has a chance ??

        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair)[::-1]: # Reverse sorted order
            stack.append((target - p) / s)

            # if theres 2 or more cars AND the 1st car in line is slower than the 2nd
            # they will become a group
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop() 
        return len(stack)
            
            



