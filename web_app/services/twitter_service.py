
import os
from pprint import pprint

from dotenv import load_dotenv
import tweepy

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print("AUTH", type(auth))

api = tweepy.API(auth)
print("API CLIENT", type(api))

#def twitter_api_client():
#    return tweepy.API(auth)

if __name__ == "__main__":

    user = api.get_user("s2t2")
    print(type(user)) #> <class 'tweepy.models.User'>
    pprint(user._json)
    print(user.id)
    print(user.screen_name)
    print(user.name)
    print(user.followers_count)

    #tweets = api.user_timeline("s2t2", tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    tweets = api.user_timeline("s2t2", tweet_mode="extended", count=150)
    print(type(tweets)) #> <class 'tweepy.models.ResultSet'>

    for tweet in tweets:
        print("-----")
        print(tweet.id, tweet.full_text)
