import slack
import time
import logging
from datetime import datetime
from mytoken import token
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Usage, Base


class HelpBot(object):
    def __init__(self):
        engine = create_engine('sqlite:///db.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

        logging.basicConfig(level=logging.INFO)
        # TODO: Might want to be able to auto join the channel
        self.mychannel = 'carchitest2'
        self.slack_client = slack.WebClient(token=token)
        logging.info("Start up")
        self.channel_id = self.get_channel_id()

    """ Slack Calls"""

    def post_message(self, message, thread_ts=None):
        # Post a message as a thread to a message
        if thread_ts is not None:
            self.slack_client.chat_postMessage(
                channel='#' + self.mychannel,
                text=message,
                thread_ts=thread_ts
            )
        # Post a message as a normal message
        else:
            self.slack_client.chat_postMessage(
                channel='#'+self.mychannel,
                text=message
            )

    def get_channel_id(self):
        list = self.slack_client.channels_list()
        for each in list.data.get('channels'):
            if each.get('name') == self.mychannel:
                return each.get('id')
        # TODO: If we can't get the channel id, we should quit
        return None

    def get_channel_history(self, oldest=None):
        if oldest is not None:
            return self.slack_client.conversations_history(channel=self.channel_id, oldest=str(oldest))
        else:
            return self.slack_client.conversations_history(channel=self.channel_id)

    def get_user(self, user_id):
        return self.slack_client.users_info(user=user_id)

    """ Database Calls"""

    def new_usage(self, message, user):
        timestamp = float(message['ts'])
        dt_object = datetime.fromtimestamp(timestamp)
        name = user['user']['profile']['real_name']
        email = user['user']['profile']['email']
        new_ts = Usage(date=dt_object, name=name, email=email)
        self.session.add(new_ts)
        self.session.commit()

    """ Other Calls """

    def parse_message(self, message):
        used = False
        if message['text']:
            message_text = message['text']
            if '404' in message_text:
                self.post_message('You Failed', thread_ts=message['ts'])
                used = True
        if used:
            self.record_metrics(message)

    def record_metrics(self, message):
        user = message['user']
        user_info = self.get_user(user)
        logging.info(str(user_info))
        self.new_usage(message, user_info)

    def run(self):
        now = time.time()
        while True:
            history = self.get_channel_history(now)
            logging.info(str(history))
            now = time.time()
            # If there are message we want to do something
            if history['messages']:
                for message in history['messages']:
                    self.parse_message(message)
            time.sleep(10)


def main():
    obj_aggr = HelpBot()
    obj_aggr.run()


if __name__ == '__main__':
    main()
