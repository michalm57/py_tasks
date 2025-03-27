# There are more pages on the web, then people on earth
# URL - Uniform Resource Locator
import urllib
from urllib import request
from urllib import parse

resp = request.urlopen("https://wikipedia.org")
print(resp.code) # Status Code 
print(resp.length) # Length of response in bytes
print(resp.peek()) # Small part of the response rather than a full value - bytes object
data = resp.read() # Read entire response

params = {"v": "EuC-yVzHhMi", "t": "5m56s"}
querystring = parse.urlencode(params)

url = "https://www.youtube.com/watch" + "?" + querystring
resp = request.urlopen(url)
resp.isclosed()
resp.code

html = resp.read().decode("utf-8")
