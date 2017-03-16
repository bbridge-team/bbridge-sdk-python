from entity import BBridgeEntity


class NLPData(BBridgeEntity):
    def __init__(self, sentences):
        """
        :type sentences: list of str
        """
        self.__sentences = sentences

    @classmethod
    def from_json(cls, json_object):
        return NLPData(json_object["sentences"])

    @property
    def sentences(self):
        return self.__sentences
