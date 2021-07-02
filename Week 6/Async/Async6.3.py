from urllib import request

url = 'http://www.bbc.com/news/business/-39135278'

data_request = request.Request(url)
response = request.urlopen(data_request)
type(responses)