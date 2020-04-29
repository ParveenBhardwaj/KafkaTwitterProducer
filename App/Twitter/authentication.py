import tweepy
from AppConfiguration.config import TwitterConfig

def get_authentication():
    '''
    Get Twitter auth
    '''
    twitter_config = TwitterConfig()
    TWITTER_APP_KEY = twitter_config.twitter_api_key
    TWITTER_APP_SECRET = twitter_config.twitter_api_secret
    TWITTER_KEY = twitter_config.twitter_access_token
    TWITTER_SECRET = twitter_config.twitter_access_token_secret

    auth = tweepy.OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_SECRET)
    auth.set_access_token(TWITTER_KEY, TWITTER_SECRET)
    return auth