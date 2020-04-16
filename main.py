from notion.client import NotionClient

client = NotionClient(token_v2="be078cd582e8b598b5a43aa13e4e7940fecc9a6915d56dedaabc1296bc7d6296e772a026be637d5dbeea4787f6c564cdcc71c8583155b5db7eac665c447747e78ed6f9c6f173216c06c74ce6fc61")

page = client.get_block("https://www.notion.so/yorsh/5309889ddccd405ea7b19472c1bf40fe?v=78cb1efa08064affae899b699703324f")


def get(self):
  name = self.request.get('name')
  state = self.request.get('state')