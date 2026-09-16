class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        res = []
        for x, y in points:
            distance = x**2 + y**2
            print(distance)
            closest.append([distance,x,y])
        heapq.heapify(closest)

        while k > 0:
            distance,x,y = heapq.heappop(closest)
            res.append([x,y])
            k -=1
        return res