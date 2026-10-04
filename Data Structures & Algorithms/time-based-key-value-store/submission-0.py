class TimeMap:

    def __init__(self):
        self.store = {} # key = string, value (pairs) = [vals, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        
        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0] # set res as the val
                l = m + 1
            else:
                # no need to set value as its greater than the last timestamp
                r = m - 1 
        return res

            
