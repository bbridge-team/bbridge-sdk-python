from json import JSONEncoder

from entity import *


class BBridgeJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, RequestId):
            return {
                "request_id": obj.request_id,
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
        elif isinstance(obj, ObjectDetectionData):
            return {
                "url": obj.url,
                "threshold": obj.threshold
            }
        elif isinstance(obj, ConceptDetectionData):
            return {
                "image_urls": obj.image_urls,
                "count": obj.count
            }
        elif isinstance(obj, ImageObjects):
            return {
                "objects": obj.objects
            }
        elif isinstance(obj, Object):
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
        elif isinstance(obj, Concepts):
            return {
                "concepts": obj.concepts,
                "error": obj.error
            }
        else:
            return super(BBridgeJSONEncoder, self).default(obj)
