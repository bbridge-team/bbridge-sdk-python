import json


class POSTagging(object):
    def __init__(self, results):
        """
        :type results: list of (list of entity.pos_tagging.POS)
        """
        self.__results = results

    @property
    def results(self):
        return self.__results

    @staticmethod
    def from_json(json_object):
        """
        :type json_object: dict
        :rtype: entity.pos_tagging.POSTagging
        """
        results = [[POS.from_json(x) for x in xs] for xs in json_object["results"]]
        return POSTagging(results)

    @staticmethod
    def from_json_str(json_string):
        """
        :type json_string: str
        :rtype: entity.pos_tagging.POSTagging
        """
        return POSTagging.from_json(json.loads(json_string))


class POS(object):
    def __init__(self, text, type_):
        """
        :type text: str
        :type type_: str
        """
        self.__text = text
        self.__type = type_

    @property
    def text(self):
        return self.__text

    @property
    def type(self):
        return self.__type

    @staticmethod
    def from_json(json_object):
        """
        :type json_object: dict
        :rtype: entity.pos_tagging.POS
        """
        return POS(json_object["text"], json_object["type"])

    @staticmethod
    def from_json_str(json_string):
        """
        :type json_string: str
        :rtype: entity.pos_tagging.POS
        """
        return POS.from_json(json.loads(json_string))
