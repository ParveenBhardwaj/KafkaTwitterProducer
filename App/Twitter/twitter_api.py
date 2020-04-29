import tweepy
from Twitter import authentication

def get_twitter_api():
    api = tweepy.API(authentication.get_authentication())
    return api