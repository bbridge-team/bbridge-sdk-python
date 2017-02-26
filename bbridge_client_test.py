import json
import unittest
import uuid
from httplib import ACCEPTED, OK

from httpretty import httpretty
from sure import expect

from bbridge_client import BBridgeClient
from entity.enum.language import EN
from entity.enum.user_attribute import GENDER, AGE_GROUP
from entity.image_concepts import ImagesConcepts, ImageConcepts
from entity.image_objects import ImageObjects, ImageObject
from entity.image_url_count import ImageURLCount
from entity.image_url_threshold import ImageURLThreshold
from entity.ner import NER
from entity.nlp_data import NLPData
from entity.pos_tagging import POSTagging, POS
from entity.response import APIResponse
from entity.sentiments import Sentiments
from entity.serialize.json_encoder import BBridgeJSONEncoder
from entity.user import User
from entity.user_profile import UserAttributes, UserProfile


def manage_httpretty(fun):
    def wrapper(*args, **kwargs):
        httpretty.enable()

        fun(*args, **kwargs)

        httpretty.disable()
        httpretty.reset()

    return wrapper


def _build_response_body(data, request_id):
    response = APIResponse(request_id, data)
    return json.dumps(response, cls=BBridgeJSONEncoder)


class BBridgeClientTest(unittest.TestCase):
    content_type = "application/json"

    token = uuid.uuid4().hex
    host_url = "http://api.bbridge.com/v1"

    client = BBridgeClient(token, host_url)

    @manage_httpretty
    def test_individual_user_profiling(self):
        expected_request_id = uuid.uuid4().hex
        expected_response = _build_response_body(UserProfile(UserAttributes("male", "AGE40_INF")), expected_request_id)
        httpretty.register_uri(httpretty.POST, "{}/profiling/personal".format(self.host_url),
                               authorization=self.token, body=expected_request_id, status=ACCEPTED)
        httpretty.register_uri(httpretty.GET, "{}/response".format(self.host_url), content_type=self.content_type,
                               authorization=self.token, body=expected_response, status=OK)

        user = User(["cat is so cute!", "Scarlet is very good person"],
                    ["https://pbs.twimg.com/media/C279-WDXEAIg4lD.jpg"])
        request_id = self.client.individual_user_profiling(user, EN, [GENDER, AGE_GROUP]).body
        response = self.client.response(request_id, UserProfile).body

        expect(json.dumps(response, cls=BBridgeJSONEncoder)).to.equal(expected_response)

    @manage_httpretty
    def test_image_objects_detection(self):
        expected_request_id = uuid.uuid4().hex
        expected_response = _build_response_body(ImageObjects([ImageObject("cat", 0.86, 200, 340, 190, 310)]),
                                                 expected_request_id)
        httpretty.register_uri(httpretty.POST, "{}/image/objects".format(self.host_url),
                               authorization=self.token, body=expected_request_id, status=ACCEPTED)
        httpretty.register_uri(httpretty.GET, "{}/response".format(self.host_url), content_type=self.content_type,
                               authorization=self.token, body=expected_response, status=OK)

        image = ImageURLThreshold("https://pbs.twimg.com/media/C279-WDXEAIg4lD.jpg", 0.7)
        request_id = self.client.image_objects_detection(image).body
        response = self.client.response(request_id, ImageObjects).body

        expect(json.dumps(response, cls=BBridgeJSONEncoder)).to.equal(expected_response)

    @manage_httpretty
    def test_image_concepts_detection(self):
        expected_request_id = uuid.uuid4().hex
        expected_response = _build_response_body(ImagesConcepts([
            ImageConcepts({"lollipop": 0.013954441, "miniskirt": 0.07939269}),
            ImageConcepts(error="Error while downloading ttps://pbs.twimg.com/media/C279-WDXEAIg4lD.jpg")
        ]), expected_request_id)
        httpretty.register_uri(httpretty.POST, "{}/image/concepts".format(self.host_url),
                               authorization=self.token, body=expected_request_id, status=ACCEPTED)
        httpretty.register_uri(httpretty.GET, "{}/response".format(self.host_url), content_type=self.content_type,
                               authorization=self.token, body=expected_response, status=OK)

        image = ImageURLCount(
            ["https://pbs.twimg.com/media/C279-WDXEAIg4lD.jpg", "ttps://pbs.twimg.com/media/C279-WDXEAIg4lD.jpg"], 5)
        request_id = self.client.image_concepts_detection(image).body
        response = self.client.response(request_id, ImagesConcepts).body

        expect(json.dumps(response, cls=BBridgeJSONEncoder)).to.equal(expected_response)

    @manage_httpretty
    def test_pos_tagging(self):
        expected_request_id = uuid.uuid4().hex
        expected_response = _build_response_body(POSTagging([[
            POS("cat", "NN"), POS("is", "VBZ"), POS("so", "RB"), POS("cute", "JJ"), POS("!", ".")
        ]]), expected_request_id)
        httpretty.register_uri(httpretty.POST, "{}/nlp/pos".format(self.host_url),
                               authorization=self.token, body=expected_request_id, status=ACCEPTED)
        httpretty.register_uri(httpretty.GET, "{}/response".format(self.host_url), content_type=self.content_type,
                               authorization=self.token, body=expected_response, status=OK)

        nlp_data = NLPData(["cat is so cute!"])
        request_id = self.client.pos_tagging(nlp_data, EN).body
        response = self.client.response(request_id, POSTagging).body

        expect(json.dumps(response, cls=BBridgeJSONEncoder)).to.equal(expected_response)

    @manage_httpretty
    def test_sentiment_analysis(self):
        expected_request_id = uuid.uuid4().hex
        expected_response = _build_response_body(Sentiments([0.7]), expected_request_id)
        httpretty.register_uri(httpretty.POST, "{}/nlp/sentiment".format(self.host_url),
                               authorization=self.token, body=expected_request_id, status=ACCEPTED)
        httpretty.register_uri(httpretty.GET, "{}/response".format(self.host_url), content_type=self.content_type,
                               authorization=self.token, body=expected_response, status=OK)

        nlp_data = NLPData(["cat is so cute!"])
        request_id = self.client.sentiment_analysis(nlp_data, EN).body
        response = self.client.response(request_id, Sentiments).body

        expect(json.dumps(response, cls=BBridgeJSONEncoder)).to.equal(expected_response)

    @manage_httpretty
    def test_named_entity_recognition(self):
        expected_request_id = uuid.uuid4().hex
        expected_response = _build_response_body(NER([[]]), expected_request_id)
        httpretty.register_uri(httpretty.POST, "{}/nlp/ner".format(self.host_url),
                               authorization=self.token, body=expected_request_id, status=ACCEPTED)
        httpretty.register_uri(httpretty.GET, "{}/response".format(self.host_url), content_type=self.content_type,
                               authorization=self.token, body=expected_response, status=OK)

        nlp_data = NLPData(["cat is so cute!"])
        request_id = self.client.name_entity_recognition(nlp_data, EN).body
        response = self.client.response(request_id, NER).body

        expect(json.dumps(response, cls=BBridgeJSONEncoder)).to.equal(expected_response)


if __name__ == '__main__':
    unittest.main()
