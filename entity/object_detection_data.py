import json


class ObjectDetectionData(object):
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
        :rtype: entity.object_detection_data.ObjectDetectionData
        """
        return ObjectDetectionData(json_object["url"], json_object["threshold"])

    @staticmethod
    def from_json_str(json_string):
        """
        :type json_string: str
        :rtype: entity.object_detection_data.ObjectDetectionData
        """
        return ObjectDetectionData.from_json(json.loads(json_string))
