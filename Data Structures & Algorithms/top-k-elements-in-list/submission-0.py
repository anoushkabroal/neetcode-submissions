class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for i in nums:
            freq_dict[i] = 1 + freq_dict.get(i, 0)
        
        min_heap = []
        for num in freq_dict.keys():
            heapq.heappush(min_heap, (freq_dict[num], num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        fin = []
        for i in range(k):
            fin.append(heapq.heappop(min_heap)[1])
        return fin