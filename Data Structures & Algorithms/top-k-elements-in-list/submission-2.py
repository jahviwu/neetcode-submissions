class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # key: num, value: amount, ex. {1: 3, 2: 2, 3: 1}
        freq = [] # bucket list, ex.  freq[1] = [3] -> Number 3 appears 1 time

        for i in range(len(nums) + 1): # length of nums + 1 to include "freq of 0"
            freq.append([]) # make them empty first because we haven't checked anything yet

        for i in nums:
            count[i] = 1 + count.get(i, 0) # Returns 0 if it doesn't exist

        for i, c in count.items(): # count.items shows all the key value pairs added to the dict
            freq[c].append(i) # the indivual value "i" occurs "c" times

        res = []
        # -1: lenght of last index
        # 0: stop at 0
        # -1: decrement (descending order)
        for i in range(len(freq) - 1, 0, - 1):
            for n in freq[i]: # for every number that occurs "i" times, add that to res
                res.append(n)
                if len(res) == k: # return all nums that occur "i" times
                    return res



