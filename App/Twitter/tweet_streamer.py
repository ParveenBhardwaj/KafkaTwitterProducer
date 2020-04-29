import tweepy
from Twitter import twitter_api
from Twitter.stream_listener import StreamListener
from KafkaProducer.kafka_producer import KafkaProducer

def get_tweet_streamer():
    kafka_producer = KafkaProducer()
    stream_listener = StreamListener(kafka_producer)
    stream = tweepy.Stream(auth=twitter_api.get_twitter_api().auth, listener=stream_listener)
    return stream