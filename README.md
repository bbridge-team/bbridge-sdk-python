# bBridge Python SDK [![Build Status](https://travis-ci.org/bbridge-team/bbridge-sdk-python.svg?branch=master)](https://travis-ci.org/bbridge-team/bbridge-sdk-python)
bBridge SDK is a Python (2 and 3) library to access the [bBridge API](http://bbridge.cloudapp.net/developer). This library enables you to make requests such as user profiling, image object detection, etc. in your Python application.

## Example
```python
from bbridge_client import BBridgeClient
from entity import User, UserProfile
from entity.enum import EN, GENDER, AGE_GROUP

# set correct user credentials
username = "username"
password = "password"

# if you have token use: BBridgeClient(token)
client = BBridgeClient.Builder(username, password).build()

# make user profiling request
user = User(["cat is so cute!", "Scarlet is very good person"],
            ["https://pbs.twimg.com/media/C279-WDXEAIg4lD.jpg"])
request_id = client.individual_user_profiling(user, EN, [GENDER, AGE_GROUP]).body

# get the request's result using 'response' method
# specify response content type by 2nd argument (e.g. UserProfiling for profile method)
response = client.response(request_id, UserProfile)

assert request_id == response.body.request_id
```

## Dependencies
```console
pip install -r requirements.txt

# for test
pip install -r test-requirements.txt
```

## Documentation
More information can be found on the [bBridge developer site](http://bbridge.cloudapp.net/developer).
