# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask
from flask import request
from notion.client import NotionClient

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def getParams():
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')

    client = NotionClient(token_v2="be078cd582e8b598b5a43aa13e4e7940fecc9a6915d56dedaabc1296bc7d6296e772a026be637d5dbeea4787f6c564cdcc71c8583155b5db7eac665c447747e78ed6f9c6f173216c06c74ce6fc61")
    page = client.get_collection_view("https://www.notion.so/yorsh/5309889ddccd405ea7b19472c1bf40fe?v=78cb1efa08064affae899b699703324f")

    row = page.collection.add_row()
    row.Имя = name
    row.Почта = email
    row.Телефон = phone
    row.Статус = "Лид"

    stroka = name + ", " + email + ", " + phone

    return (stroka)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
