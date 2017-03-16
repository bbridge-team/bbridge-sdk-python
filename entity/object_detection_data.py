from entity import BBridgeEntity


class ObjectDetectionData(BBridgeEntity):
    def __init__(self, url, threshold):
        """
        :type url: str
        :type threshold: float
        """
        self.__url = url
        self.__threshold = threshold

    @classmethod
    def from_json(cls, json_object):
        return ObjectDetectionData(json_object["url"], json_object["threshold"])

    @property
    def url(self):
        return self.__url

    @property
    def threshold(self):
        return self.__threshold
