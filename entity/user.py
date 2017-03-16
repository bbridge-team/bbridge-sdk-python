from entity import BBridgeEntity


class User(BBridgeEntity):
    def __init__(self, text=[], image_urls=[]):
        """
        :type text: list of str
        :type image_urls: list of str
        """
        self.__text = text
        self.__image_urls = image_urls

    @classmethod
    def from_json(cls, json_object):
        return User(json_object.get("text"), json_object.get("image_urls"))

    @property
    def text(self):
        return self.__text

    @property
    def image_urls(self):
        return self.__image_urls
