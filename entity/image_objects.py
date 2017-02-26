import json


class ImageObjects(object):
    def __init__(self, objects):
        """
        :type objects: list of entity.image_objects.ImageObject
        """
        self.__objects = objects

    @property
    def objects(self):
        return self.__objects

    @staticmethod
    def from_json(json_object):
        """
        :type json_object: dict
        :rtype: entity.image_objects.ImageObjects
        """
        objects = [ImageObject.from_json(x) for x in json_object["objects"]]
        return ImageObjects(objects)

    @staticmethod
    def from_json_str(json_string):
        """
        :type json_string: str
        :rtype: entity.image_objects.ImageObjects
        """
        return ImageObjects.from_json(json.loads(json_string))


class ImageObject(object):
    def __init__(self, cls_name, score, x, y, w, h):
        """
        :type cls_name: str
        :type score: float
        :type x: int
        :type y: int
        :type w: int
        :type h: int
        """
        self.__cls_name = cls_name
        self.__score = score
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h

    @property
    def cls_name(self):
        return self.__cls_name

    @property
    def score(self):
        return self.__score

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def w(self):
        return self.__w

    @property
    def h(self):
        return self.__h

    @staticmethod
    def from_json(json_object):
        """
        :type json_object: dict
        :rtype: entity.image_objects.ImageObject
        """
        return ImageObject(json_object["cls_name"], json_object["score"], json_object["x"], json_object["y"],
                           json_object["w"], json_object["h"])

    @staticmethod
    def from_json_str(json_string):
        """
        :type json_string: str
        :rtype: entity.image_objects.ImageObject
        """
        return ImageObject.from_json(json.loads(json_string))
