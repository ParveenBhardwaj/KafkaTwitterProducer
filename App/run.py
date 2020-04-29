from Twitter import tweet_streamer
from KafkaProducer.kafka_producer import KafkaProducer

if __name__ == "__main__":
    print('Start Streaming')
    try:
        stream = tweet_streamer.get_tweet_streamer()
        stream.filter(track=['covid', 'covid19', 'coronavirus'])
    except KeyboardInterrupt:
        print("Stopped Streaming")
    finally:
        stream.disconnect()