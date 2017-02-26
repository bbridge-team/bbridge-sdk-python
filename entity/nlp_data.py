import json


class NLPData(object):
    def __init__(self, sentences):
        """
        :type sentences: list of str
        """
        self.__sentences = sentences

    @property
    def sentences(self):
        return self.__sentences

    @staticmethod
    def from_json(json_object):
        """
        :type json_object: dict
        :rtype: entity.nlp_data.NLPData
        """
        return NLPData(json_object["sentences"])

    @staticmethod
    def from_json_str(json_string):
        """
        :type json_string: str
        :rtype: entity.nlp_data.NLPData
        """
        return NLPData.from_json(json.loads(json_string))
