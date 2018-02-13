from bbridge_sdk.entity.response.bbridge_entity import BBridgeEntity

class DataId(BBridgeEntity):
    def __init__(self, value):
        """
        :type value: str
        """
        self.__value = value

    @classmethod
    def from_json(cls, json_object):
        return cls(json_object["value"])

    @property
    def value(self):
        return self.__value
