import json


class ImagesConcepts(object):
    def __init__(self, results):
        """
        :type results: list of entity.image_concepts.Concepts
        """
        self.__results = results

    @property
    def results(self):
        return self.__results

    @staticmethod
    def from_json(json_object):
        """
        :type json_object: dict
        :rtype: entity.image_concepts.ImagesConcepts
        """
        results = [Concepts.from_json(x) for x in json_object["results"]]
        return ImagesConcepts(results)

    @staticmethod
    def from_json_str(json_string):
        """
        :type json_string: str
        :rtype: entity.image_concepts.ImagesConcepts
        """
        return ImagesConcepts.from_json(json.loads(json_string))


class Concepts(object):
    def __init__(self, concepts=None, error=None):
        """
        :type concepts: dict | None
        :type error: str | None
        """
        self.__concepts = concepts
        self.__error = error

    @property
    def concepts(self):
        return self.__concepts

    @property
    def error(self):
        return self.__error

    @staticmethod
    def from_json(json_object):
        """
        :type json_object: dict
        :rtype: entity.image_concepts.Concepts
        """
        return Concepts(json_object.get("concepts"), json_object.get("error"))

    @staticmethod
    def from_json_str(json_string):
        """
        :type json_string: str
        :rtype: entity.image_concepts.Concepts
        """
        return Concepts.from_json(json.loads(json_string))
