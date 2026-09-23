class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {} # freq of each number
        freq = [[] for i in range(len(nums) + 1)] # empty list with max freq == len(nums) so it must go up to it

        for n in nums:
            count[n] = 1 + count.get(n, 0) # increments count of each n
        for n, c in count.items():
            freq[c].append(n) # appends n to sublist at index c in freq

        res = [] # result empty list
        for i in range(len(freq) - 1, 0, -1): # iterates backwards from most freq to least
            for n in freq[i]: # checks what numbers are in this freq (ex. 2 and 3 are in freq[4] since they happen 4 times)
                res.append(n) # add n (most freq number)
                if len(res) == k: # if we added k number of freqs stop
                    return res


