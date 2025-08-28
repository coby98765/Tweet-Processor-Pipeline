from nltk.sentiment.vader import SentimentIntensityAnalyzer
from data_loader.load_txt import Loader
import re

class DataProcessing:
    def __init__(self):
        self.weapons = Loader.load_weapons()

    def tweets_info(self,tweet):
        tweet['sentiment'] = self.post_sentiment(tweet['clean_text'])
        tweet['weapons_detected'] = self.detected_weapons(tweet['clean_text'])
        tweet['relevant_timestamp'] = self.find_timestamp(tweet['original_text'])
        return tweet

    @staticmethod
    def post_sentiment(tweet):
        score = SentimentIntensityAnalyzer().polarity_scores(tweet)
        if score['compound'] > 0.5:
            return 'positive'
        if score['compound'] < -0.5:
            return 'negative'
        else:
            return "neutral"

    def detected_weapons(self,tweet):
        weapons_detected = []
        for weapon in self.weapons:
            if weapon in tweet.lower():
                weapons_detected.append(weapon)
        return weapons_detected

    @staticmethod
    def find_timestamp(tweet):
        # Regex
        pattern = r"\b\d{4}-\d{2}-\d{2}(?:\s\d{2}:\d{2}:\d{2})?\b"
        match = re.findall(pattern, tweet)
        if match:
            latest_date = max(match)
            return latest_date
        return ''

