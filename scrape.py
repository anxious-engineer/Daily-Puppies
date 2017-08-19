import urllib, json
import webbrowser

subreddits = [
    'dogpictures',
    'eyebleach',
    'aww'
]

start_doc = '<!DOCTYPE html>\n<html>\n<title>Puppies</title>\n<head>\n</head>\n<body>\n<div id=\'photos\'>\n'

tags = ''

end_doc = '</div>\n</body>\n<footer>\n<p>Developed by: <a href="../">David Parsons</a>\n</br>\n<a href="http://github.com/Parsons-David/Puppy-Scraper">Source</a>\n</p>\n</footer>\n</html>'

def get_posts(subreddit, limit=None):
    url = 'https://www.reddit.com/r/%s/top/.json' % subreddit

    if limit:
        url += '?limit=%d' % limit

    print('Reading... %s' % url)

    data = json.loads(urllib.urlopen(url).read())

    if('error' in data.keys()):
        return {}

    # print(data)

    posts = data['data']['children']
    print('%d Posts Read' % len(posts))

    return posts

def save_image(url):
    global tags
    f = open('docs/imgs/' + url.split('/')[-1],'wb')
    tags += '<img src=\'%s\'' % ('imgs/' + url.split('/')[-1])
    tags += ' height="500">\n</br>\n'
    f.write(urllib.urlopen(url).read())
    f.close()

# def send_image(url):

if __name__=='__main__':

    for sub in subreddits:

        sub_posts = get_posts(sub, 10)

        for post in sub_posts:
            image_url = post['data']['url'].encode('utf-8')
            print('Opening... %s' % image_url)

            if image_url.endswith('.jpg') or image_url.endswith('.gif'):
                save_image(image_url)


            # else:
            #     webbrowser.open(image_url)

    f = open('docs/index.html', 'wb')
    f.write(start_doc + tags + end_doc)
    f.close()
