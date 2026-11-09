import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Sort trips based on the start location
        trips.sort(key=lambda t: t[1])
        minHeap = []
        currpass = 0
        
        for t in trips:
            numpass, start, end = t
            while minHeap and minHeap[0][0] <= start:
                currpass -= minHeap[0][1]
                heapq.heappop(minHeap)
                
            currpass += numpass
            
            if currpass > capacity:
                return False
                
            heapq.heappush(minHeap, [end, numpass])
            
        return True