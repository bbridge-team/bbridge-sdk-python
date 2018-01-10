from .bbridge_entity import BBridgeEntity


class Data(BBridgeEntity):
    def __init__(self, json):
        """
        :type json: str
        """
        self.__json = json

    @classmethod
    def from_json(cls, json_object):
        return cls(json_object["json"])

    @property
    def json(self):
        return self.__json
