#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "946421467-GOYcByChetsA4dbacsBF8imgv34Q6NOKxP7fTcFa"
access_token_secret = "2xVEq0zoMMZHaIo8HidtT6bkGYj526fwA4foXYnvMURhj"
consumer_key = "rF1UhAhVJsmie822K1bXN5lvd"
consumer_secret = "UykH43jgHn5SWYHTprLyfrQPWKl7V2ODu2MhJVTqIJosjbLn5a"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filters Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])

