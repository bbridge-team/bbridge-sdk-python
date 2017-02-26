import json


class NER(object):
    def __init__(self, results):
        """
        :type results: list of (list of entity.ner.Entity)
        """
        self.__results = results

    @property
    def results(self):
        return self.__results

    @staticmethod
    def from_json(json_object):
        """
        :type json_object: dict
        :rtype: entity.ner.NER
        """
        results = [[Entity.from_json(x) for x in xs] for xs in json_object["results"]]
        return NER(results)

    @staticmethod
    def from_json_str(json_string):
        """
        :type json_string: str
        :rtype: entity.ner.NER
        """
        return NER.from_json(json.loads(json_string))


class Entity(object):
    def __init__(self, count, text, type_):
        """
        :type count: int
        :type text: str
        :type type_: str
        """
        self.__count = count
        self.__text = text
        self.__type = type_

    @property
    def count(self):
        return self.__count

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
        :rtype: entity.ner.Entity
        """
        return Entity(json_object["count"], json_object["text"], json_object["type"])

    @staticmethod
    def from_json_str(json_string):
        """
        :type json_string: str
        :rtype: entity.ner.Entity
        """
        return NER.from_json(json.loads(json_string))
