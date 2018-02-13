from .bbridge_entity import BBridgeEntity


class DataIdResult(BBridgeEntity):
    def __init__(self, data_id, crawled_at):
        """
        :type data_id: str
        :type crawled_at: long
        """
        self.__data_id = data_id
        self.__crawled_at = crawled_at

    @classmethod
    def from_json(cls, json_object):
        return DataIdResult(json_object["data_id"], json_object["crawled_at"])

    @property
    def data_id(self):
        return self.__data_id

    @property
    def crawled_at(self):
        return self.__crawled_at
