class Solution(object):
    def findKthLargest(self, nums, k):
        minHeap = []
        heapify(minHeap)

        for ele in nums:
            heappush(minHeap, ele)
            if len(minHeap) > k:
                heappop(minHeap)
        return minHeap[0]
        