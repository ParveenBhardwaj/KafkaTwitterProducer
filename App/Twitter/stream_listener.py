import tweepy

class StreamListener(tweepy.StreamListener):
    def __init__(self, kafka_producer):
        super(StreamListener,self).__init__()
        self._kafka_producer = kafka_producer

    def on_status(self, status):
        self._kafka_producer.send_message(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            return False