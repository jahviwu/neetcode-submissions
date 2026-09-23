class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list) # char count to list of anagrams
        
        for s in strs:
            count = [0] * 26 # 26 letters

            for char in s:
                count[ord(char) - ord("a")] += 1 # if a = 80, 80 - 80 + 1 = 1, b = 2

            result[tuple(count)].append(s)

        return list(result.values())