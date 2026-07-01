class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = {}
        self.followMap = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
        
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        if userId not in self.followMap:
            self.followMap[userId] = set()
        
        followees = set(self.followMap[userId])
        followees.add(userId)

        for followeeId in followees:
            if followeeId in self.tweetMap and self.tweetMap[followeeId]:
                idx = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][idx]
                minHeap.append([count,tweetId, followeeId, idx-1])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId)

            if idx >=0:
                next_count, next_tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(minHeap, [next_count, next_tweetId,followeeId, idx-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
