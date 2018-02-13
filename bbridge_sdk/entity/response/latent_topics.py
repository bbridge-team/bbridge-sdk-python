from .bbridge_entity import BBridgeEntity

class LatentTopics(BBridgeEntity):
    def __init__(self, topicsList):
        """
        :type topicsList: list[bbridge_sdk.entity.response.latent_topics.TopicDistribution]
        """
        self.__topicsList = topicsList

    @classmethod
    def from_json(cls, json_object):
        return [TopicDistribution.from_json(x) for x in json_object["topics_list"]]

    @property
    def topicsList(self):
        return self.__topicsList

class TopicDistribution(BBridgeEntity):
    def __init__(self, topics=None):
        """
        :type topics: dict | None
        """
        self.__topics = topics

    @classmethod
    def from_json(cls, json_object):
        return TopicDistribution(json_object.get("topics"))

    @property
    def topics(self):
        return self.__topics
