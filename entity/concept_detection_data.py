from entity import BBridgeEntity


class ConceptDetectionData(BBridgeEntity):
    def __init__(self, image_urls, count):
        """
        :type image_urls: list of str
        :type count: int
        """
        self.__image_urls = image_urls
        self.__count = count

    @classmethod
    def from_json(cls, json_object):
        return cls(json_object["image_urls"], json_object["count"])

    @property
    def image_urls(self):
        return self.__image_urls

    @property
    def count(self):
        return self.__count
