import urllib, json

response = urllib.urlopen('https://www.reddit.com/r/dogpictures/top/.json').read()
data = json.loads(response)

listings = data['data']['children']

for l in listings:
    print(l['data']['url'])
