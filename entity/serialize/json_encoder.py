from json import JSONEncoder

from entity import APIResponse
from entity import ImageObjects, ImageObject
from entity import ImageURLCount
from entity import ImageURLThreshold
from entity import ImagesConcepts, ImageConcepts
from entity import NER, Entity
from entity import NLPData
from entity import POSTagging, POS
from entity import Sentiments
from entity import User
from entity import UserAttributes, UserProfile


class BBridgeJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, APIResponse):
            return {
                "requestId": obj.request_id,
                "content": obj.content
            }
        elif isinstance(obj, User):
            return {
                "text": obj.text,
                "image_urls": obj.image_urls
            }
        elif isinstance(obj, UserProfile):
            return {
                "profiling": obj.profiling
            }
        elif isinstance(obj, UserAttributes):
            return {
                "gender": obj.gender,
                "age_group": obj.age_group,
                "relationship": obj.relationship,
                "education_level": obj.education_level,
                "income": obj.income,
                "occupation": obj.occupation
            }
        elif isinstance(obj, NER):
            return {
                "results": obj.results
            }
        elif isinstance(obj, Entity):
            return {
                "count": obj.count,
                "text": obj.text,
                "type": obj.type
            }
        elif isinstance(obj, Sentiments):
            return {
                "results": obj.results
            }
        elif isinstance(obj, POSTagging):
            return {
                "results": obj.results
            }
        elif isinstance(obj, POS):
            return {
                "text": obj.text,
                "type": obj.type
            }
        elif isinstance(obj, NLPData):
            return {
                "sentences": obj.sentences
            }
        elif isinstance(obj, ImageURLThreshold):
            return {
                "url": obj.url,
                "threshold": obj.threshold
            }
        elif isinstance(obj, ImageURLCount):
            return {
                "image_urls": obj.image_urls,
                "count": obj.count
            }
        elif isinstance(obj, ImageObjects):
            return {
                "objects": obj.objects
            }
        elif isinstance(obj, ImageObject):
            return {
                "cls_name": obj.cls_name,
                "score": obj.score,
                "x": obj.x,
                "y": obj.y,
                "w": obj.w,
                "h": obj.h
            }
        elif isinstance(obj, ImagesConcepts):
            return {
                "results": obj.results
            }
        elif isinstance(obj, ImageConcepts):
            return {
                "concepts": obj.concepts,
                "error": obj.error
            }
        else:
            return super(BBridgeJSONEncoder, self).default(obj)
