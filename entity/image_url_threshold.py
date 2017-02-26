import json


class ImageURLThreshold(object):
    def __init__(self, url, threshold):
        """
        :type url: str
        :type threshold: float
        """
        self.__url = url
        self.__threshold = threshold

    @property
    def url(self):
        return self.__url

    @property
    def threshold(self):
        return self.__threshold

    @staticmethod
    def from_json(json_object):
        """
        :type json_object: dict
        :return: entity.image_url_threshold.ImageURLThreshold
        """
        return ImageURLThreshold(json_object["url"], json_object["threshold"])

    @staticmethod
    def from_json_str(json_string):
        """
        :type json_string: str
        :return: entity.image_url_threshold.ImageURLThreshold
        """
        return ImageURLThreshold.from_json(json.loads(json_string))
