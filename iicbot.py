
import tweepy

key= '1291773532511309824-fYbvdPI9ejI1FbA9RSxxzwLwFSajQP'
secret= 'zcTxT3Z0f6J5iRRtX0xMuuhYTsGwsU58X1jiOJoZhwSCA'

consumer_key= 'aGVJkAgpgtBNHnKdfGR9oxZCV'
consumer_secret= 'R5QVKD7SvT7fi099dopNXd8rW7fdBdsYDkxnr6qMUGRVH70gUj'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key,secret)

api= tweepy.API(auth)
tweets= api.mentions_timeline()
print(tweets[0].text)