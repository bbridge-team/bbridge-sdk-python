# bBridge Python SDK for SoMin Analytics
[![Build Status](https://travis-ci.org/bbridge-team/bbridge-sdk-python.svg?branch=master)](https://travis-ci.org/bbridge-team/bbridge-sdk-python)
[![Latest Stable Version](https://img.shields.io/pypi/v/bbridge_sdk.svg)](https://pypi.python.org/pypi/bbridge_sdk)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/bbridge-team/bbridge-sdk-python/master/LICENSE)

bBridge SDK is a Python (2 and 3) library to access the [SoMin API](http://dev.somin.ai). This library enables user to make requests such as user profiling, image object detection, etc. from a Python application.

## Installation

```bash
pip install bbridge_sdk
```

## Example
```python
from __future__ import print_function

from bbridge_sdk import BBridgeClient
from bbridge_sdk.entity.request import User
from bbridge_sdk.entity.response import UserProfile
from bbridge_sdk.entity.enum import EN, GENDER, AGE_GROUP

# set correct user credentials
username = "username"
password = "password"

# if you have token use: BBridgeClient(token)
client = BBridgeClient.Builder(username, password).build()

# make user profiling request
user = User(["cat is so cute!", "Scarlet is very good person"],
            ["https://pbs.twimg.com/media/C279-WDXEAIg4lD.jpg"])
request_id = client.individual_user_profiling(user, EN, [GENDER, AGE_GROUP]).body.request_id

# get the request's result using 'response' method
# specify response content type by 2nd argument (e.g. UserProfiling for profile method)
response = client.response(request_id, UserProfile)

print(response.body.profiling.gender)
```

## Dependencies
```console
pip install -r requirements.txt

# for test
pip install -r test-requirements.txt
```

## Documentation
More information can be found on the [SoMin developer site](http://dev.somin.ai).
