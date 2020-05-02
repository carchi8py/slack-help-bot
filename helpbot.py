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

    def post_message(self, message):
        self.slack_client.chat_postMessage(
            channel='#'+self.mychannel,
            text=message
        )

    def run(self):
        self.post_message("Test message")


def main():
    obj_aggr = HelpBot()
    obj_aggr.run()


if __name__ == '__main__':
    main()
