from json import JSONEncoder

from bbridge_sdk.entity.request.documnets_data import DocumentsData
from ..request import *


class BBridgeJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {
                "text": obj.text,
                "image_urls": obj.image_urls
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
        elif isinstance(obj, DocumentsData):
            return {
                "documents": obj.documents,
                "count": obj.count
            }
        else:
            return super(BBridgeJSONEncoder, self).default(obj)
