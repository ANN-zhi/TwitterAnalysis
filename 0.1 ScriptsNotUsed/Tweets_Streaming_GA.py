# Twitter Data Collection with Streaming API - by Atlas

import sys
import csv
import tweepy
import warnings
import datetime
import os
import json
from HTMLParser import HTMLParser

# account information 
consumer_key="kLOp9riBEBEmIylc5fmAP73Qj"
consumer_secret="gW6f33HU3aHR7aYu9AqVz0LWzGlDSBd1CSyoQR4cw4hhHuFCcu"
access_key="780826417198043137-LjkAfbTk0rFArKvQmzjRiuDvWCiP55o"
access_secret="12hOtElVTxQs2xFUYEXKCzAXOGXbjHoHUgVhYQD66IRWW"

# access twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# steam listener class
class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
      
        # start a new file after every 10000 tweets
        if count%10000==0:
            print count
            date_time=datetime.datetime.now().strftime('%Y%m%d_%H%M')
            print date_time            
            output_file="twitter_"+date_time+".csv" # output file name
            csvFile = open(output_file, 'wb')
            global csvWriter
            csvWriter=csv.writer(csvFile)
            csvWriter.writerow(['id', 'created_at', 'text','lang','lat','long','place','userid','screenname','name','image'])

        try:
            dict=status.coordinates
#       if status.place:
            csvWriter.writerow([status.id, status.created_at, status.text.encode('utf-8'), status.lang, \
                                                    dict['coordinates'][1],dict['coordinates'][0],status.place.full_name, status.author.id_str.encode('utf-8'), \
                                                    status.user.screen_name,status.user.name,status.user.profile_image_url_https])
            global count
            count+=1
            print count,":       ",status.text.encode('utf-8')

        except Exception as e:
            print e
            pass
        
    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # don't kill the stream

###############
    
if __name__ == '__main__':

    error_time=0
    while True:
        try:
            # initialization
            default_stdout = sys.stdout
            default_stderr = sys.stderr
            reload(sys)
            sys.stdout = default_stdout
            sys.stderr = default_stderr
            sys.setdefaultencoding('utf-8')
            warnings.filterwarnings("ignore")

            # create directory and create first file
            directory="C:\\Twitter" # directory
            if not os.path.exists(directory):
                os.makedirs(directory)
            os.chdir(directory)
            date_time=datetime.datetime.now().strftime('%Y%m%d_%H%M')
            output_file="twitter_"+date_time+".csv" # output file name
            csvFile = open(output_file, 'wb')
            csvWriter = csv.writer(csvFile)
            csvWriter.writerow(['id', 'created_at', 'text','lang','lat','long','place','userid','screenname','name','image'])
            print "Run at "+date_time
            
            # start the stream
            count=0
            streamingAPI = tweepy.streaming.Stream(auth, CustomStreamListener())
            streamingAPI.filter(languages=["en"],locations=[-85.61,30.36,-80.75,35.0])
            
        except Exception, e: # print error time before restart
            print e
            error_time+=1
            print "Error Time: "+str(error_time)
            print "=================================================================="
