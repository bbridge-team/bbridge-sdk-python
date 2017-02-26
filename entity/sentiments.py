import json


class Sentiments(object):
    def __init__(self, results):
        """
        :type results: list of float
        """
        self.__results = results

    @property
    def results(self):
        return self.__results

    @staticmethod
    def from_json(json_object):
        """
        :type json_object: dict
        :rtype: entity.sentiments.Sentiments
        """
        return Sentiments(json_object["results"])

    @staticmethod
    def from_json_str(json_string):
        """
        :type json_string: str
        :rtype: entity.sentiments.Sentiments
        """
        return Sentiments.from_json(json.loads(json_string))
