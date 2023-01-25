import tweepy
API_KEY = "AAAAAAAAAAAAAAAAAAAAAIgFbwEAAAAAHxTIUaGi%2FtiXlfsxfBfTeqCJd5o%3Dqx9JTCsYvIqYsNJx573wC4bwjDKGdmAoc0eaaUtYdpOwFHYrY8"

client = tweepy.Client(API_KEY)

query = "covid"

response = client.search_recent_tweets(query)
out = open("tweets.txt", "w")

for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten(limit=5000):
    out.write(tweet.text.replace("\n","") + ("\n"))
    