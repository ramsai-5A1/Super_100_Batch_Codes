
class Solution(object):
    def kClosest(self, points, k):
        result = []
        maxHeap = []
        heapify(maxHeap)
        
        for index in range(len(points)):
            x, y = points[index][0], points[index][1]
            distance = (x * x) + (y * y)
            heappush(maxHeap, [-1 * distance, index])
            if len(maxHeap) > k:
                heappop(maxHeap)
                
        while maxHeap:
            index = heappop(maxHeap)[1]
            result.append(points[index])

        return result