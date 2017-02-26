# bBridge Python SDK

## Example
```python
# set correct user credentials
username = "username"
password = "password"

# if you have token use: BBridgeClient(token)
client = BBridgeClient.Builder(username, password).build()

# make user profiling request
user = User(["cat is so cute!", "Scarlet is very good person"],
            ["https://pbs.twimg.com/media/C279-WDXEAIg4lD.jpg"])
request_id = client.individual_user_profiling(user, "en", ["gender", "age_group"]).body

# get the request's result using 'response' method
# specify response content type by 2nd argument (e.g. UserProfiling for profile method)
response = client.response(request_id, UserProfile)

assert request_id == response.body.request_id
```

## Also
Visit our [developer site](http://bbridge.cloudapp.net/developer) to find more information.
