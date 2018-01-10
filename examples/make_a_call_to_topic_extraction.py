from __future__ import print_function

from bbridge_sdk import BBridgeClient
from bbridge_sdk.entity.enum import EN
from bbridge_sdk.entity.enum.domain import INSURANCE, GENERAL
from bbridge_sdk.entity.request.documnets_data import DocumentsData

# set correct user credentials
from active_response_retrieval import active_response_retrieval

username = "<USER>"
password = "<PASSWORD>"

# if you have token use: BBridgeClient(token)
client = BBridgeClient.Builder(username, password).build()

# make topic detection request
documents = DocumentsData([["For the precise calculation of your report we may need an estimation of your age and location. \
You can share your results with your friends but we will never share your answers or your facebook information."]], 5)
request_id = client.topic_detection(documents, EN, INSURANCE).body.request_id

active_response_retrieval(client, request_id)
