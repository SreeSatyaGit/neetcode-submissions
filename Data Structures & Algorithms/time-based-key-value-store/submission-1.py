class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, val: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((val, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        values = self.store[key]
        l, r = 0, len(values) - 1
        res = ""
        
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]  # Store the value, not the timestamp
                l = m + 1
            else:
                r = m - 1
                
        return res