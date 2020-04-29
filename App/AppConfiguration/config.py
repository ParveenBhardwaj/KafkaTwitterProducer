from AppConfiguration.config_base import ConfigBase

class KafkaConfig(ConfigBase):
    '''
    Defines Kafka Configuration
    '''
    def __init__(self):
        super().__init__('Kafka')

    @property
    def bootstrap_servers_address(self):
        return self.get_property('BootstrapServersAddress')

    @property
    def first_topic_name(self):
        return self.get_property('FirstTopicName')

class TwitterConfig(ConfigBase):
    '''
    Defines Twitter Configuration
    '''
    def __init__(self):
        super().__init__('Twitter')

    @property
    def twitter_api_key(self):
        return self.get_property('TwitterApiKey')

    @property
    def twitter_api_secret(self):
        return self.get_property('TwitterApiSecret')

    @property
    def twitter_access_token(self):
        return self.get_property('TwitterAccessToken')

    @property
    def twitter_access_token_secret(self):
        return self.get_property('TwitterAccessTokenSecret')