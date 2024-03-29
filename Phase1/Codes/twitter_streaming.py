# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables that contains the user credentials to access Twitter API
access_token = "1093621382125113344-7joxv0TjNVRV4tKfFuhqehICrpNYiU"
access_token_secret = "TfHaGPIMiprK3TIYbS5Xxn9gBTpGtSMPRORWfkMb4BTTy"
consumer_key = "gOswpASuUh6kgobzq1X0yM7lB"
consumer_secret = "MQsoyqvfgfnbeuxBdKVFfgixTNc1pUbTkxgTKCjfIfwhbEcEDA"


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print
        data
        saveFile = open(r'twiterdata.csv', 'a')
        saveFile.write(data)
        saveFile.write('\n')
        saveFile.close()

    def on_error(self, status):
        print
        status


if __name__ == '__main__':
    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['rgv', 'SDLive', 'Kentucky', 'realDonaldTrump', 'narendramodi', 'Cristiano', 'BarackObama',
                         'justinbieber', 'katyperry', 'Rihanna', 'taylorswift', 'ladygaga', 'TheEllenShow',
                         'jtimberlake', 'BillGates', 'CNN', 'BBCBreaking', 'iamsrk', 'SrBachchan', 'imVkohli', 'NBA',
                         'pitbull', 'deepikapadukone', 'HillaryClinton', 'LeoDiCaprio', 'selenagomez'])
