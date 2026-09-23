class Solution:

    # we are encoding with a number to indicate the length of each word
    # Ex. Food -> 4 -> Encoded: 4#Food

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 # increment until we find #
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length]) # from j (#) + 1 (after the pound) to the rest of the word
            i = j + 1 + length # move pointer i (which was at 0 to the end of the first word)
        return res