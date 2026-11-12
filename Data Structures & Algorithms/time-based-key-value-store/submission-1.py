class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        left, right = 0, len(self.timemap[key]) - 1
        result = ""

        while left <= right:
            mid = left + (right - left) // 2
            stored_timestamp, stored_value = self.timemap[key][mid]

            if stored_timestamp > timestamp:
                right = mid - 1
            else:
                result = stored_value
                left = mid + 1

        return result
        
        
        