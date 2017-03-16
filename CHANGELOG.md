# v0.2 (2017-03-15)

### Breaking changes from v0.1

* All POST requests (e.g. user profiling) return RequestId class now instead of pure request id.
  ```python
  request_id = client.individual_user_profiling(user, EN, [GENDER]).body.request_id
  ```

* APIResponse class was removed (Response method returns the unwrapped result)

* Rename the following classes:
    * *ImageURLCount* → *ConceptDetectionData*
    * *ImageURLThreshold* → *ObjectDetectionData*
    * *ImageConcepts* → *Concepts*
    * *ImageObject* → *Object*

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