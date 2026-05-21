class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequency count
        res = defaultdict(int)

        for num in nums:
            res[num] += 1
        
        heap = []
        for num, count in res.items():
            heapq.heappush(heap, (count, num))

            # if heap too big, remove smallest
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for count, num in heap]
