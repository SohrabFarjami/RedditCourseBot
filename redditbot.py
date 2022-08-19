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
           'best way to learn python', ('python', 'course', 'beginner')]

subreddit = reddit.subreddit("learnpython")

for post in subreddit.new(limit=10):
    post_lower = post.title.lower()
    if any(
        all(w in post_lower for w in word) if isinstance(word, tuple) 
        else word in post_lower 
        for word in keyword):
            text_file = open(("id.txt"),'a+')
            if not (post.id in text_file.read()):
                text_file = open(("id.txt") , "a+")
                text_file.write('' + "\n")
                text_file.write(post.id)
                text_file.close()
                print(post.id)
                post.reply((Here you go)('https://www.reddit.com/r/learnpython/wiki/index/#wiki_new_to_programming.3F'))
                time.sleep(660)
                    else:
                print('Already Checked')

