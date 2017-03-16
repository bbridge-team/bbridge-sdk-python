from entity import BBridgeEntity


class POSTagging(BBridgeEntity):
    def __init__(self, results):
        """
        :type results: list of (list of entity.pos_tagging.POS)
        """
        self.__results = results

    @classmethod
    def from_json(cls, json_object):
        results = [[POS.from_json(x) for x in xs] for xs in json_object["results"]]
        return POSTagging(results)

    @property
    def results(self):
        return self.__results


class POS(BBridgeEntity):
    def __init__(self, text, type_):
        """
        :type text: str
        :type type_: str
        """
        self.__text = text
        self.__type = type_

    @classmethod
    def from_json(cls, json_object):
        return POS(json_object["text"], json_object["type"])

    @property
    def text(self):
        return self.__text

    @property
    def type(self):
        return self.__type
