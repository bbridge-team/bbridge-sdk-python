import json


class BBridgeEntity(object):
    @classmethod
    def from_json(cls, json_object):
        """
        :type json_object: dict
        :rtype: entity.bbridge_entity.BBridgeEntity
        """
        raise NotImplementedError

    @classmethod
    def from_json_str(cls, json_string):
        """
        :type json_string: str
        :rtype: entity.bbridge_entity.BBridgeEntity
        """
        return cls.from_json(json.loads(json_string))
