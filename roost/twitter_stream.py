# Class that attaches to the Twitter Streaming API

import pycurl, json, sys

STREAM_URL = "http://stream.twitter.com/1/statuses/filter.json"

USER = None # should be a string
PASS = None # should be a string

#TRACK_TERMS = "track=i want for christmas"
TRACK_TERMS = "track=birthday"

TIMEOUT = 60*60*3

class TwitterStreamingAPI:

	def __init__(self):
		# TODO: load credentials from profile file
	
		self.buffer = ""
		self.conn = pycurl.Curl()
		self.conn.setopt(pycurl.USERPWD, "%s:%s" % (USER, PASS))
		self.conn.setopt(pycurl.URL, STREAM_URL)
		self.conn.setopt(pycurl.POST, True)
		self.conn.setopt(pycurl.WRITEFUNCTION, self.on_receive)
		self.conn.setopt(pycurl.TIMEOUT, TIMEOUT)
		config_file = json.loads(open(sys.argv[1], 'r').readline())
		self.outputfile = config_file['outputfile']
		self.conn.setopt(pycurl.POSTFIELDS, TRACK_TERMS)
		self.conn.perform()

	def start(self):
		pass

	def on_receive(self, data):
		self.buffer += data
		if data.endswith("\r\n") and self.buffer.strip():
			tweet = self.buffer
			try:
				content = json.loads(self.buffer)			 
				self.buffer = ""
				with open(self.outputfile, 'ab') as f:
					f.write(tweet.replace('\n','') + '\n')
			except:
				sys.exit(1)

if __name__ == '__main__':
	pass