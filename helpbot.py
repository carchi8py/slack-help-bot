import slack
import time
import logging
from mytoken import token


class HelpBot(object):
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        # TODO: Might want to be able to auto join the channel
        self.mychannel = 'carchitest2'
        self.slack_client = slack.WebClient(token=token)
        logging.info("Start up")
        self.channel_id = self.get_channel_id()

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

    def parse_message(self, message):
        if message['text']:
            message_text = message['text']
            if '404' in message_text:
                self.post_message('You Failed', thread_ts=message['ts'])

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
