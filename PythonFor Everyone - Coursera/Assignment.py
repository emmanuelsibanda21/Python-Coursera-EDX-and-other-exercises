import urllib
import json
#open url and store content in variable handle
handle = urllib.urlopen('http://python-data.dr-chuck.net/comments_315754.json')
#read content and store read content in variable read_handle
read_handle = handle.read()
#parse and deserialize json to python object and store in variable parsed_handle
parsed_handle = json.loads(read_handle)
#extract the comment counts from dict and add all numbers contained in count
sum(comments.get('count',0) for comments in parsed_handle['comments'])
