
import tweepy
import time

print('this is my twitter bot', flush=True)
key= '1544641062517768192-3drwsbauGzpUZx0x5pGRq3l97bcwqV'
secret= 'CWizjORrVOP8bIXNUiszq7wxcxtDPvNJnz6VLeeqpxGhq'

consumer_key= 'mLrV33CLVZTrmVIFllIcN2EYX'
consumer_secret= 'B0foTOoHo7PoLHjgGXypVcEGT23RMYsy96SlzT2FbRjftbxnZS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key,secret)
api = tweepy.API(auth)
file_name = 'last_seen_id.txt'
def retrieve_last_seen_id(file_name):
  f_read = open(file_name, 'r')
  last_seen_id = int(f_read.read().strip())
  f_read.close()
  return last_seen_id
def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return
def reply_to_tweets():
  print('retrieving and replying to tweets...', flush=True)
last_seen_id = retrieve_last_seen_id(file_name)
mentions = api.mentions_timeline(since_id=last_seen_id(file_name),tweet_mode='extended')
for mention in reversed(mentions):
 print(str(mention.id) + ' - ' + mention.full_text, flush=True)
last_seen_id = mention.id
store_last_seen_id(last_seen_id, file_name)
if '#helloworld' in mention.full_text.lower():
 print('found #helloworld!', flush=True)
 print('responding back...', flush=True)
api.update_status('@' + mention.user.screen_name +
'#HelloWorld back to you!', mention.id)

while True:
 reply_to_tweets()
 time.sleep(15)
