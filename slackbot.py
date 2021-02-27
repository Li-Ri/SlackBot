from tokens import Tokens
import slack
import os 
from pathlib import Path
from scraper import Reddit

token = Tokens()

slack_token = token['slack_token']



class SlackAPI: 

    def __init__(self):

        self.client = slack.WebClient(token=slack_token)

    def send_message(self, messages):

        for message in messages:
            self.client.chat_postMessage(
                channel='# working-on-a-bot-to-help-my-cohort',
                text=message
            )

    



if __name__=='__main__':

    cl = SlackAPI()

    cl.send_message('Hey ya cunt')