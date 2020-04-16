from notion.client import NotionClient
from flask import Flask
import requests

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def get(self):
  name = self.request.get('name')
  email = self.request.get('email')
  print (name,email)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]

client = NotionClient(token_v2="be078cd582e8b598b5a43aa13e4e7940fecc9a6915d56dedaabc1296bc7d6296e772a026be637d5dbeea4787f6c564cdcc71c8583155b5db7eac665c447747e78ed6f9c6f173216c06c74ce6fc61")

page = client.get_block("https://www.notion.so/yorsh/5309889ddccd405ea7b19472c1bf40fe?v=78cb1efa08064affae899b699703324f")


