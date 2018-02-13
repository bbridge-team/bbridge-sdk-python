from json import JSONEncoder

from bbridge_sdk.entity.request.documnets_data import DocumentsData
from bbridge_sdk.entity.request.user_id import UserID
from bbridge_sdk.entity.request.data_id import DataId
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
        elif isinstance(obj, DataId):
            return {
                "value": obj.value
            }
        elif isinstance(obj, UserID):
            return {
                "user_name": obj.user_name,
                "data_source": obj.data_source,
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
