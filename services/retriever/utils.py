class Utils:

    @staticmethod
    def normalize_objects(tweet_list):
        for tweet in tweet_list:
            tweet['id'] = str(tweet.pop('_id'))
            # tweet['TweetID'] = str(int(tweet['TweetID']))
            x = tweet.pop('TweetID')
            tweet["CreateDate"] = tweet["CreateDate"].isoformat()
            tweet['original_text'] = tweet.pop('text')
        return tweet_list