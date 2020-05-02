import slack
import time
import logging
from mytoken import token


class HelpBot(object):
    def __init__(self):
        logging.basicConfig()
        # TODO: Might want to be able to auto join the channel
        self.mychannel = 'carchitest2'
        self.slack_client = slack.WebClient(token=token)
        self.channel_id = self.get_channel_id()

    def post_message(self, message):
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

    def get_channel_history(self):
        return self.slack_client.conversations_history(channel=self.channel_id)

    def run(self):
        self.post_message("Test message")
        history = self.get_channel_history()
        if history['messages']:
            for message in history['messages']:
                if message['text']:
                    print(str(message['text']))


def main():
    obj_aggr = HelpBot()
    obj_aggr.run()


if __name__ == '__main__':
    main()
