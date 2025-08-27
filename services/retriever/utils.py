class Utils:

    @staticmethod
    def normalize_objects(tweet_list):
        for tweet in tweet_list:
            tweet['_id'] = str(tweet['_id'])
            tweet['TweetID'] = str(int(tweet['TweetID']))
            tweet["CreateDate"] = tweet["CreateDate"].isoformat()
        return tweet_list