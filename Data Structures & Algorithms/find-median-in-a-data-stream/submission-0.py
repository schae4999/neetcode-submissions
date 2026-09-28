class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        if not self.small:
            heapq.heappush(self.small, -num)
        elif num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)
        elif len(self.large) > len(self.small) + 1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)
        
    def findMedian(self) -> float:
        # Case 1: small has more elements
        if len(self.small) > len(self.large):
            return -self.small[0]
        # Case 2: large has more elements
        elif len(self.large) > len(self.small):
            return self.large[0]
        # Case 3: same number of elements
        else:
            small_max = -self.small[0]
            large_min = self.large[0]
            return (small_max + large_min) / 2
        
        