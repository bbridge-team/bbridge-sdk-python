# v0.3 (2017-04-08)

### Breaking changes from v0.2

* All packages start with ```bbridge_sdk``` now.

### Features

* SDK upload into PyPI, so use ```pip install bbridge_sdk``` to install it

# v0.2 (2017-03-15)

### Breaking changes from v0.1

* All POST requests (e.g. user profiling) return RequestId class now instead of pure request id.
  ```python
  request_id = client.individual_user_profiling(user, EN, [GENDER]).body.request_id
  ```

* APIResponse class was removed (Response method returns the unwrapped result)

* Changed constructor arguments order of Response class:
  ```python
  def __init__(self, status_code, body=None, err_message=None):
    ...
  ```

* Renamed the following classes:
    * *ImageURLCount* → *ConceptDetectionData*
    * *ImageURLThreshold* → *ObjectDetectionData*
    * *ImageConcepts* → *Concepts*
    * *ImageObject* → *Object*

* Split entities into two packages: *response* and *request*

### Features

* All bBridge entity classes inherit BBridgeEntity class

# v0.1 (2017-03-03)

### First release of bBridge Python SDK

This inaugural release implements the following API methods:

* Response
* Individual user profiling
* Image objects/concepts detection
* Part of speech tagging
* Sentiment analysis
* Named-entity recognition

Also, this release includes all entities required for the requests mentioned above.