
import praw
from tokens import Tokens
class Reddit:

    def __init__(self):

        Token=Tokens()

        self.reddit = praw.Reddit(
            client_id = Token['client_id'],
            client_secret= Token['client_secret'],
            user_agent= 'my-user-agent',
            username=Token['username'],
            password=Token['password']
            )

    def subreddit(self, subreddit, query):
        
        keyMap = {}

        for submission in self.reddit.subreddit('learnpython+learnprogramming').search('module import error'):
            keyMap[submission.title] = submission.url

        return keyMap


if __name__ == '__main__':
    ins = Reddit()

    search = ins.subreddit('learnpython','')
    print(search)