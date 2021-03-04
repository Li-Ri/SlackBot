import pandas
import praw
from praw.models import MoreComments
from tokens import Tokens
import itertools

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

    def subreddit_keyMap(self, subreddit, query):

        keyMap = {}
   
        for submission in self.reddit.subreddit(subreddit).search(query):
            keyMap[submission.title] = {'url':submission.url,
                                        'comments': submission.num_comments}
      
        return keyMap

    def sort_comments(self,subreddit, query):

        keyMap = self.subreddit_keyMap(subreddit, query)
        sorted_comments = {}

        for sub in keyMap:
            
            num_comments = keyMap[sub].get('comments', 0)
            if num_comments > 10:
                sorted_comments[sub] = keyMap[sub].get('url', 0)
            else:
                pass
        



    
        return dict(itertools.islice(sorted_comments.items(),5))


    
              


        


if __name__ == '__main__':
    ins = Reddit()
    print(ins.sort_comments('learnpython', 'module not found'))
    # search = ins.subreddit_urls('learnpython','module error')
    # ins.comment_count(search)