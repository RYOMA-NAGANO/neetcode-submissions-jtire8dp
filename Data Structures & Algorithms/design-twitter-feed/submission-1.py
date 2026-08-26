class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap, res = [], []
        users = self.following[userId] | {userId}
        for uid in users:
            if self.tweets[uid]:
                index = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][index]
                heapq.heappush(heap, (-time, tweetId, uid, index))
        while heap and len(res) < 10:
            negTime, tweetId, uid, index = heapq.heappop(heap)
            res.append(tweetId)
            index -= 1
            if index >= 0:
                time, tweetId = self.tweets[uid][index]
                heapq.heappush(heap, (-time, tweetId, uid, index))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
