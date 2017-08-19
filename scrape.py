import urllib, json
import webbrowser

subreddits = [
    'dogpictures',
    'eyebleach',
    'aww'
]

def get_posts(subreddit, limit=None):
    url = 'https://www.reddit.com/r/%s/top/.json' % subreddit

    if limit:
        url += '?limit=%d' % limit

    print('Reading... %s' % url)

    data = json.loads(urllib.urlopen(url).read())

    print(data.keys())

    # print(data)

    posts = data['data']['children']
    print('%d Posts Read' % len(posts))

    return posts

def save_picture(url):
    f = open('imgs/' + url.split('/')[-1],'wb')
    f.write(urllib.urlopen(url).read())
    f.close()

if __name__=='__main__':

    for sub in subreddits:

        sub_posts = get_posts(sub, 4)

        for post in sub_posts:
            image_url = post['data']['url'].encode('utf-8')
            print('Opening... %s' % image_url)

            if image_url.endswith('.jpg') or image_url.endswith('.gif'):
                save_picture(image_url)

            # webbrowser.open(image_url)
