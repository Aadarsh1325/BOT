from pickle import TRUE
import tweepy
import time

key= '1544641062517768192-3drwsbauGzpUZx0x5pGRq3l97bcwqV'
secret= 'CWizjORrVOP8bIXNUiszq7wxcxtDPvNJnz6VLeeqpxGhq'

consumer_key= 'mLrV33CLVZTrmVIFllIcN2EYX'
consumer_secret= 'B0foTOoHo7PoLHjgGXypVcEGT23RMYsy96SlzT2FbRjftbxnZS'

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
    tweets = api.mentions_timeline(since_id=read_last_seen(FILE_NAME),tweet_mode='extended')
    for tweet in reversed(tweets):
      if '#panchayat' in tweet.full_text:
        print(str(tweet.id) + ' - ' + tweet.full_text)
        api.update_status('@'+ tweet.user.screen_name + " BHAKK OCDK",in_reply_to_status_id=tweet.id)
        api.create_favorite(tweet.id)
        api.retweet(tweet.id)
        store_last_seen(FILE_NAME, tweet.id)

while TRUE:
   reply()
   time.sleep(2)