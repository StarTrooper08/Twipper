#import tweepy module
import tweepy

#Creating the authentication object
consumer_key='consumer key will be added here'
consumer_secret='consumer secret key will be added here'
access_token='access token will be added here'
access_token_secret='access token secret key will be added here'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
#Setting your access token and secret
auth.set_access_token(access_token,access_token_secret)
#Creating the API object while passing in auth information
api=tweepy.API(auth)
#public_tweets
public_tweets =api.home_timeline()

name="PMOIndia"
#Number of tweets to pull
tweetCount=10
#Calling the user_timelins function with our parameters
results=api.user_timeline(id=name,count=tweetCount)
print("tweets pulled")
#foreach through all tweets pulled
i=1
for tweet in results:
    #printing the text stored inside the tweet object
    print("Tweet no is",i)
    print(tweet.text)
    i=i+1

