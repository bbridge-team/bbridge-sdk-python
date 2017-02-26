import json


class User(object):
    def __init__(self, text=[], image_urls=[]):
        """
        :type text: list of str
        :type image_urls: list of str
        """
        self.__text = text
        self.__image_urls = image_urls

    @property
    def text(self):
        return self.__text

    @property
    def image_urls(self):
        return self.__image_urls

    @staticmethod
    def from_json(json_object):
        """
        :type json_object: dict
        :rtype: entity.user.User
        """
        return User(json_object.get("text"), json_object.get("image_urls"))

    @staticmethod
    def from_json_str(json_string):
        """
        :type json_string: str
        :rtype: entity.user.User
        """
        return User.from_json(json.loads(json_string))
