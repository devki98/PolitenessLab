import time
from slackclient import SlackClient
from vaderSentiment import SentimentIntensityAnalyzer

# replace this with your code.
slack_client = SlackClient('xoxb-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
starterbot_id = None

RTM_READ_DELAY = 1

def parse_event(slack_events):
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            return event["text"], event["channel"], event["ts"]
    return None, None, None

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        analyzer = SentimentIntensityAnalyzer()
        while True:
            text, channel, timestamp = parse_event(slack_client.rtm_read())
            if text != None:
                vs = analyzer.polarity_scores(text)
                str = "{:-<30} {}".format(text, str(vs))
                comp_str = str.find("'compound':")
                print(comp_str)
                substr_comp = str[comp_str: ]
                print(substr_comp)
                colon = substr_comp.find(":")
                comp_val = float(str[colon: len(str) ])
                print(comp_val)
                if (comp_val < -0.05):
                    response = "maybe try sending something a little nicer!"
                if (comp_val > 0.05)
                    response = "this is a positive statement
                response = "this is a neutral statement"
                slack_client.api_call(
                    "chat.postMessage",
                    channel=channel,
                    text=response
                )
                slack_client.api_call(
                    "chat.update",
                    channel=channel,
                    ts=timestamp,
                    text="dontknow"
                )
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")


# https://www.fullstackpython.com/blog/build-first-slack-bot-python.html
# https://github.com/cjhutto/vaderSentiment#installation
