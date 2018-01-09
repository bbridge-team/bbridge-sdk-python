from .bbridge_entity import BBridgeEntity

class Topics(BBridgeEntity):
    def __init__(self, results):
        """
        :type results: list[map[bbridge_sdk.entity.response.ner.Entity]]
        """
        self.__results = results

    @classmethod
    def from_json(cls, json_object):
        results = [[Entity.from_json(x) for x in xs] for xs in json_object["results"]]
        return Topics(results)

    @property
    def results(self):
        return self.__results
