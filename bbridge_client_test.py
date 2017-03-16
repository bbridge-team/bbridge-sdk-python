import json
import unittest
import uuid

from httpretty import httpretty
from sure import expect

from bbridge_client import BBridgeClient
from entity import *
from entity.enum import *
from entity.serialize import BBridgeJSONEncoder


def manage_httpretty(fun):
    def wrapper(*args, **kwargs):
        httpretty.enable()

        fun(*args, **kwargs)

        httpretty.disable()
        httpretty.reset()

    return wrapper


def _build_response_body(data):
    return json.dumps(data, cls=BBridgeJSONEncoder)


class BBridgeClientTest(unittest.TestCase):
    content_type = "application/json"

    token = uuid.uuid4().hex
    host_url = "http://api.bbridge.com/v1"

    client = BBridgeClient(token, host_url)

    @manage_httpretty
    def test_individual_user_profiling(self):
        expected_request_id = uuid.uuid4().hex
        expected_response = _build_response_body(UserProfile(UserAttributes("male", "AGE40_INF")))
        httpretty.register_uri(httpretty.POST, "{}/profiling/personal".format(self.host_url),
                               authorization=self.token,
                               body=json.dumps(RequestId(expected_request_id), cls=BBridgeJSONEncoder), status=202)
        httpretty.register_uri(httpretty.GET, "{}/response".format(self.host_url), content_type=self.content_type,
                               authorization=self.token, body=expected_response, status=200)

        user = User(["cat is so cute!", "Scarlet is very good person"],
                    ["https://pbs.twimg.com/media/C279-WDXEAIg4lD.jpg"])
        request_id = self.client.individual_user_profiling(user, EN, [GENDER, AGE_GROUP]).body.request_id
        response = self.client.response(request_id, UserProfile).body

        expect(json.dumps(response, cls=BBridgeJSONEncoder)).to.equal(expected_response)

    @manage_httpretty
    def test_image_objects_detection(self):
        expected_request_id = uuid.uuid4().hex
        expected_response = _build_response_body(ImageObjects([Object("cat", 0.86, 200, 340, 190, 310)]))
        httpretty.register_uri(httpretty.POST, "{}/image/objects".format(self.host_url),
                               authorization=self.token,
                               body=json.dumps(RequestId(expected_request_id), cls=BBridgeJSONEncoder), status=202)
        httpretty.register_uri(httpretty.GET, "{}/response".format(self.host_url), content_type=self.content_type,
                               authorization=self.token, body=expected_response, status=200)

        image = ObjectDetectionData("https://pbs.twimg.com/media/C279-WDXEAIg4lD.jpg", 0.7)
        request_id = self.client.image_objects_detection(image).body.request_id
        response = self.client.response(request_id, ImageObjects).body

        expect(json.dumps(response, cls=BBridgeJSONEncoder)).to.equal(expected_response)

    @manage_httpretty
    def test_image_concepts_detection(self):
        expected_request_id = uuid.uuid4().hex
        expected_response = _build_response_body(ImagesConcepts([
            Concepts({"lollipop": 0.013954441, "miniskirt": 0.07939269}),
            Concepts(error="Error while downloading ttps://pbs.twimg.com/media/C279-WDXEAIg4lD.jpg")
        ]))
        httpretty.register_uri(httpretty.POST, "{}/image/concepts".format(self.host_url),
                               authorization=self.token,
                               body=json.dumps(RequestId(expected_request_id), cls=BBridgeJSONEncoder), status=202)
        httpretty.register_uri(httpretty.GET, "{}/response".format(self.host_url), content_type=self.content_type,
                               authorization=self.token, body=expected_response, status=200)

        image = ConceptDetectionData(
            ["https://pbs.twimg.com/media/C279-WDXEAIg4lD.jpg", "ttps://pbs.twimg.com/media/C279-WDXEAIg4lD.jpg"], 5)
        request_id = self.client.image_concepts_detection(image).body.request_id
        response = self.client.response(request_id, ImagesConcepts).body

        expect(json.dumps(response, cls=BBridgeJSONEncoder)).to.equal(expected_response)

    @manage_httpretty
    def test_pos_tagging(self):
        expected_request_id = uuid.uuid4().hex
        expected_response = _build_response_body(POSTagging([[
            POS("cat", "NN"), POS("is", "VBZ"), POS("so", "RB"), POS("cute", "JJ"), POS("!", ".")
        ]]))
        httpretty.register_uri(httpretty.POST, "{}/nlp/pos".format(self.host_url),
                               authorization=self.token,
                               body=json.dumps(RequestId(expected_request_id), cls=BBridgeJSONEncoder), status=202)
        httpretty.register_uri(httpretty.GET, "{}/response".format(self.host_url), content_type=self.content_type,
                               authorization=self.token, body=expected_response, status=200)

        nlp_data = NLPData(["cat is so cute!"])
        request_id = self.client.pos_tagging(nlp_data, EN).body.request_id
        response = self.client.response(request_id, POSTagging).body

        expect(json.dumps(response, cls=BBridgeJSONEncoder)).to.equal(expected_response)

    @manage_httpretty
    def test_sentiment_analysis(self):
        expected_request_id = uuid.uuid4().hex
        expected_response = _build_response_body(Sentiments([0.7]))
        httpretty.register_uri(httpretty.POST, "{}/nlp/sentiment".format(self.host_url),
                               authorization=self.token,
                               body=json.dumps(RequestId(expected_request_id), cls=BBridgeJSONEncoder), status=202)
        httpretty.register_uri(httpretty.GET, "{}/response".format(self.host_url), content_type=self.content_type,
                               authorization=self.token, body=expected_response, status=200)

        nlp_data = NLPData(["cat is so cute!"])
        request_id = self.client.sentiment_analysis(nlp_data, EN).body.request_id
        response = self.client.response(request_id, Sentiments).body

        expect(json.dumps(response, cls=BBridgeJSONEncoder)).to.equal(expected_response)

    @manage_httpretty
    def test_named_entity_recognition(self):
        expected_request_id = uuid.uuid4().hex
        expected_response = _build_response_body(NER([[]]))
        httpretty.register_uri(httpretty.POST, "{}/nlp/ner".format(self.host_url),
                               authorization=self.token,
                               body=json.dumps(RequestId(expected_request_id), cls=BBridgeJSONEncoder), status=202)
        httpretty.register_uri(httpretty.GET, "{}/response".format(self.host_url), content_type=self.content_type,
                               authorization=self.token, body=expected_response, status=200)

        nlp_data = NLPData(["cat is so cute!"])
        request_id = self.client.name_entity_recognition(nlp_data, EN).body.request_id
        response = self.client.response(request_id, NER).body

        expect(json.dumps(response, cls=BBridgeJSONEncoder)).to.equal(expected_response)


if __name__ == '__main__':
    unittest.main()
