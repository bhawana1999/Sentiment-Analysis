from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey="H6fv9sJdKI8zYbc0WcA0KEgwt"
csecret="UOKijxSqY4YPUz4d56ACNuyCU7YE8EpFoo0jOhNWFqBLRaCBUi"
atoken="748102140145573888-VKzjzgToLt0nACVkwkFX5YtZE0ng7ay"
asecret="m6TLB9i9FnX8TFbRsIfKSjocHloeBPMYXPuswv3H4zYvW"

#from twitterapistuff import *

class listener(StreamListener):

    def on_data(self, data):

        all_data = json.loads(data)

        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)

        if confidence*100 >= 80:

            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()

        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])
