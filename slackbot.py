from tokens import Tokens
import slack
import os 
from pathlib import Path
from scraper import Reddit
from flask import Flask
from slackeventsapi import SlackEventAdapter

token = Tokens()

slack_token = token['slack_token']

app = Flask(__name__)

slack_event_adaptor = SlackEventAdapter(token['signing_secret'], '/slack/events',app)

client = slack.WebClient(token=slack_token)
BOT_ID = client.api_call('auth.test')['user_id']

reddit = Reddit()

@slack_event_adaptor.on('message')
def message(payload):
    
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
        

    comments = reddit.sort_comments('learnpython', text)

    message = ''
    print(user_id)
    for comment in comments.keys():
       
        url = comments[comment]
        message+=f'{comment}: {url}'

    if BOT_ID!=user_id and not message:
        pass
    elif BOT_ID!=user_id and message:
            client.chat_postMessage(
            channel=channel_id,
            text=message
            )
            


        




    





if __name__=='__main__':

    app.run(debug=True)