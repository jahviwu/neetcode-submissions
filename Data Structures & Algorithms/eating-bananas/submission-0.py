class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min of 1 bananas per hour, max of the greatest val in piles
        # ex. [1, 27, 3, 2] -> max = 27 so it can clear all bananas per pile in one go which would be 4 hours
        l, r = 1, max(piles) 
        res = r # Set answer to max val for now 

        while l <= r:
            m = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / m) # math.ceil rounds up, needed bc if 11 bananas / 4 bananas per hour = 2.75 -> 3 hours at least 

            if hours <= h: # if koko can clear all bananas in time before target
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res