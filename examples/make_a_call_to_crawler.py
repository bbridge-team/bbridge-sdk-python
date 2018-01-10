from __future__ import print_function

import time

from bbridge_sdk import BBridgeClient
from bbridge_sdk.entity.enum.data_source import TWITTER
from bbridge_sdk.entity.request.user_id import UserID

from bbridge_sdk.entity.response.data_id import DataId
from active_response_retrieval import active_response_retrieval

username = "<ELEVATED_USER>"
password = "<PASSWORD>"

# if you have token use: BBridgeClient(token)
client = BBridgeClient.Builder(username, password).build()

# make crawling request
userId = UserID(TWITTER, "farseevs")
request_id = client.crawler_retrieval(userId, 10, "TEST").body.request_id

time.sleep(10)
# get the request's result using 'response' method
# specify response content type by 2nd argument (e.g. DataId for crawling method)
response = client.response(request_id, DataId)

# make data retrieval request (requires elevated user rights)
request_id = client.crawler_download(DataId(response.body.value)).body.request_id

active_response_retrieval(client, request_id)
