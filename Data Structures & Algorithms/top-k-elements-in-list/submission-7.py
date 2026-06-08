class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = []
        counts = Counter(nums)
        heapq.heapify_max(arr)
        for val,freq in counts.items():
            heapq.heappush_max(arr, (freq, val))
        res = heapq.nlargest(k, counts.keys(), key=counts.get)
        return res
        