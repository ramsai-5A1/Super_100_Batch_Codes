class Solution(object):
    def leastInterval(self, tasks, n):
        store = dict()
        for task in tasks:
            if task not in store:
                store[task] = 1 
            else:
                store[task] += 1 
                
        maxHeap = []
        heapify(maxHeap)
        
        for task in store.keys():
            heappush(maxHeap, [-1 * store[task], task])
            
        blockedTasks = []
        timer = 0
        while maxHeap or blockedTasks:
            if maxHeap:
                curr = heappop(maxHeap)
                curr[0] *= -1
                curr[0] -= 1 
                if curr[0] > 0:
                    blockedTasks.append([-1 * curr[0], curr[1], timer + n])
              
            if blockedTasks and blockedTasks[0][2] == timer:
                heappush(maxHeap, [blockedTasks[0][0], blockedTasks[0][1]])
                blockedTasks.pop(0)
            timer += 1         
        
        return timer     
        
        
        
        
        
        
        
        