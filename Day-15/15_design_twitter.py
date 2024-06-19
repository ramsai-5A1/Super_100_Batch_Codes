
class Node:
    def __init__(self):
        self.followersList = set()
        self.tweets = []


class Twitter(object):

    def __init__(self):
        self.db = dict()
        self.timer = 1
        for i in range(1, 501):
            self.db[i] = Node()
        

    def postTweet(self, userId, tweetId):
        obj = self.db[userId]
        obj.tweets.append([self.timer, tweetId])
        if len(obj.tweets) > 10:
            obj.tweets = obj.tweets[1:]
        self.timer += 1
        

    def getNewsFeed(self, userId):
        result = []
        maxHeap = []
        heapify(maxHeap)
        tweets = self.db[userId].tweets 
        for tweet in tweets:
            heappush(maxHeap, [tweet[0], tweet[1]])
            if len(maxHeap) > 10:
                heappop(maxHeap)

        for followee in self.db[userId].followersList:
            obj = self.db[followee]
            for tweet in obj.tweets:
                heappush(maxHeap, [tweet[0], tweet[1]])
                if len(maxHeap) > 10:
                    heappop(maxHeap)

        while maxHeap:
            curr = heappop(maxHeap)
            result.append(curr[1])
        result = result[::-1]
        return result
        

    def follow(self, followerId, followeeId):
        obj = self.db[followerId]
        obj.followersList.add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        obj = self.db[followerId]
        if followeeId in obj.followersList:
            obj.followersList.remove(followeeId)