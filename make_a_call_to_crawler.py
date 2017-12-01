from __future__ import print_function

import time

from bbridge_sdk import BBridgeClient
from bbridge_sdk.entity.enum.data_source import TWITTER
from bbridge_sdk.entity.request.user_id import UserID

from bbridge_sdk.entity.response.data import Data
from bbridge_sdk.entity.response.data_id import DataId

# set correct user credentials
username = "<ELEVATED_USER_NAME>"
password = "<ELEVATED_PASSWORD>"

# if you have token use: BBridgeClient(token)
client = BBridgeClient.Builder(username, password).build()

# make user profiling request
userId = UserID(TWITTER, "farseevs")
request_id = client.crawler_retrieval(userId, 10, "TEST").body.request_id

time.sleep(3)
# get the request's result using 'response' method
# specify response content type by 2nd argument (e.g. UserProfiling for profile method)
response = client.response(request_id, DataId)

request_id = client.crawler_download(DataId(response.body.value)).body.request_id
time.sleep(1)

response = client.response(request_id)

print(response.body)
