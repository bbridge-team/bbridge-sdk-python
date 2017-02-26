from json import JSONEncoder

from entity.image_concepts import ImagesConcepts, ImageConcepts
from entity.image_objects import ImageObjects, ImageObject
from entity.image_url_count import ImageURLCount
from entity.image_url_threshold import ImageURLThreshold
from entity.ner import NER, Entity
from entity.nlp_data import NLPData
from entity.pos_tagging import POSTagging, POS
from entity.response import APIResponse
from entity.sentiments import Sentiments
from entity.user import User
from entity.user_profile import UserAttributes, UserProfile


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
