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
           'best way to learn python', ('python', 'course', 'beginner'), ('beginner', 'course')]

subreddit = reddit.subreddit("learnpython")

for post in subreddit.new(limit=200):
    post_lower = post.title.lower()
    if any(
        all(w in post_lower for w in word) if isinstance(word, tuple) 
        else word in post_lower 
        for word in keyword):
            with open('id.txt') as myfile:
                if not post.id in myfile.read():
                    text_file = open(("id.txt") , "a")
                    text_file.write('' + "\n")
                    text_file.write(post.id)
                    text_file.close()
                    print(post.id)
                    post.reply("[Here you go](https://www.reddit.com/r/learnpython/wiki/index/#wiki_new_to_programming.3F])\n\n This reply was made by a bot. You can check my code [Here](https://github.com/SohrabFarjami/RedditCourseBot)")
                    time.sleep(660)
                    
                else:
                     print('Already checked')
