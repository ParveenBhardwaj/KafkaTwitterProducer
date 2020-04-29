# Kafka Twitter Producer
A Kafka producer that streams tweets from Twitter live, and pushes them into a Kafka Cluster.
Written in Python.

# Installation
Install python version 3.7 or above
Install following python libraries:
1. tweepy
2. confluent-kafka

# Setup
Create a Twitter Developer acount, and get the secret keys required to authenticate with Twitter's APIs. This might be helpful: https://stackoverflow.com/questions/1808855/getting-new-twitter-api-consumer-and-secret-keys

Rename 'config_sample.json' to 'config.json' and add your values.

# Usage
Navigate to the App folder, and run the run.py
