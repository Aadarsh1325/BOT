
from pickle import TRUE
import tweepy
import time


key= '1291773532511309824-fYbvdPI9ejI1FbA9RSxxzwLwFSajQP'
secret= 'zcTxT3Z0f6J5iRRtX0xMuuhYTsGwsU58X1jiOJoZhwSCA'

consumer_key= 'aGVJkAgpgtBNHnKdfGR9oxZCV'
consumer_secret= 'R5QVKD7SvT7fi099dopNXd8rW7fdBdsYDkxnr6qMUGRVH70gUj'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key,secret)

api= tweepy.API(auth)

FILE_NAME = "last_seen.txt"

def read_last_seen(FILE_NAME):
            file_read = open(FILE_NAME, 'r')
            last_seen_id= int(file_read.read().strip())
            file_read.close()
            return last_seen_id

       
def store_last_seen(FILE_NAME, last_seen_id):
            file_write = open(FILE_NAME, 'w')
            file_write.write (str(last_seen_id))
            file_write.close()
            return 

           
def reply():
        tweets =api.mentions_timeline(read_last_seen(FILE_NAME),tweet_mode='extended')
        #tweets = api.mentions_timeline(since_id=read_last_seen(FILE_NAME), tweet_mode='extended')
        for tweet in reversed(tweets):
            if '#BOTTT' in tweet.full_text.lower():
                print(str(tweet.id) + ' - ' + tweet.full_text)
                api.update_status('@' + tweet.user.screen_name + "Auto reply is perfectly working", tweet.id)
                api.create_favorite(tweet.id)
                api.retweet(tweet.id)
                store_last_seen(FILE_NAME, tweet.id)

while TRUE:
    reply()
    time.sleep(5)
                
print("ajsj")               