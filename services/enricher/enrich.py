from nltk.sentiment.vader import SentimentIntensityAnalyzer
from data_loader.load_txt import Loader
import re

class DataProcessing:
    def __init__(self,tweet):
        self.tweet = tweet

    def tweets_info(self):
        self.tweet['sentiment'] = self.post_sentiment(self.tweet['clean_text'])
        self.tweet['weapons_detected'] = self.detected_weapons(self.tweet['clean_text'])
        self.tweet['relevant_timestamp'] = self.find_timestamp(self.tweet['original_text'])
        return self.tweet

    @staticmethod
    def post_sentiment(tweet):
        score = SentimentIntensityAnalyzer().polarity_scores(tweet)
        if score['compound'] > 0.5:
            return 'positive'
        if score['compound'] < -0.5:
            return 'negative'
        else:
            return "neutral"

    @staticmethod
    def detected_weapons(tweet):
        weapons = Loader.load_weapons()
        for weapon in weapons:
            if weapon in tweet.lower().split():
                return weapon
        return ''

    @staticmethod
    def find_timestamp(tweet):
        # Regex
        pattern = r"\b\d{4}-\d{2}-\d{2}(?:\s\d{2}:\d{2}:\d{2})?\b"
        match = re.search(pattern, tweet)
        if match:
            return match.group()
        return ''

