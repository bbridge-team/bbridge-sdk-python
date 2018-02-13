from __future__ import print_function
import time

from bbridge_sdk import BBridgeClient
from bbridge_sdk.entity.enum.data_source import TWITTERMULTISOURCE, TWITTER, INSTAGRAM, EMAIL
from bbridge_sdk.entity.request.user_id import UserID
from bbridge_sdk.entity.request.data_id import DataId

from bbridge_sdk.entity.response.data_id_result import DataIdResult
from active_response_retrieval import active_response_retrieval

NUM_CRAWL = 100

username = "developer"
password = "12345"

client = BBridgeClient.Builder(username, password).build()

userId = UserID(TWITTERMULTISOURCE, "farseevs")
request_id = client.crawler_retrieval(userId, NUM_CRAWL, "TEST").body.request_id

time.sleep(NUM_CRAWL / 5)

response = client.response(request_id, DataIdResult)

request_id = client.crawler_download(DataId(response.body.data_id)).body.request_id

active_response_retrieval(client, request_id)
