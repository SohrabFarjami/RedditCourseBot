import praw
import time

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="",
    username='',
    password=''
)


keyword = ['learn python', 'learn a python language',
           'best way to learn python' ]

subreddit = reddit.subreddit("learnpython")

for post in subreddit.new(limit=10):
    post_lower = post.title.lower()
    if any(word in post_lower for word in keyword):
        print(post_lower)
        post.reply('https://www.reddit.com/r/learnpython/wiki/index/#wiki_new_to_programming.3F')
        time.sleep(660)
