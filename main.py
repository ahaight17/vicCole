# IMPORTS 
import tweepy
import json

# CONSTANTS
GOFUNDME = 'https://gf.me/u/ytcx4p'
LOGS = open('logs.txt', 'a+')

# setup api keys to work with 
keysFile = open('keys.json')
keys = keysFile.read();
keys = json.loads(keys)

# auth
auth = tweepy.OAuthHandler(keys['api_key'], keys['api_secret'])
auth.set_access_token(keys['access_token'], keys['access_secret'])

# API object is core of tweepy
api = tweepy.API(auth)

fo = open('mytest.txt', 'w+');
tweets = {}
public_tweets = api.home_timeline()
for tweet in public_tweets:
    tweets[tweet.author.screen_name] = tweet.id


responses = []
for i in tweets:
    status = api.update_status('@' + i + ' testing', int(tweets[i]))
    fo.write(status.id_str + '\n')
    responses.append(status.id)
    responses.append(tweets[i])

for i in range (0, len(responses)):
    LOGS.write(str(responses[i]) + '\n')
    if i%2 != 0:
        LOGS.write('\n')
fo.close()




# fo2 = open('mytest.txt', 'r')
# while True:
#     line = fo2.readline()
#     if line == '':
#         break
#     api.destroy_status(int(line))

#if __name__ == '__main__':