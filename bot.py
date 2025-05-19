import slack
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Currently testing with different Slack Workspace
# TODO: Add UBC Sailbot Access Token to .env
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

client.chat_postMessage(channel='#bot-test', text="Hello Asvin!")