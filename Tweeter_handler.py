#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import tweepy



#Variables that contains the user credentials to access Twitter API 
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#api.followers('screen_name')

#print(api)

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

print("List of all the followers of screen name deepanshu sharma")
#To get list of all followers
for user in tweepy.Cursor(api.followers, screen_name="deepanshu sharma").items():
    print user.screen_name
print("List of all the following of screen name deepanshu sharma")
#To get the list of all following users
for user in tweepy.Cursor(api.friends, screen_name="deepanshu sharma").items():
    print user.screen_name




