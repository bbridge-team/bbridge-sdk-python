import json
import unittest
import uuid

from httpretty import httpretty
from sure import expect

from bbridge_sdk.bbridge_client import BBridgeClient
from bbridge_sdk.entity.enum import *
from bbridge_sdk.entity.enum.domain import INSURANCE
from bbridge_sdk.entity.request import *
from bbridge_sdk.entity.request.documnets_data import DocumentsData
from bbridge_sdk.entity.response import *
from bbridge_sdk.entity.response.latent_topics import LatentTopics, TopicDistribution


def manage_httpretty(fun):
    def wrapper(*args, **kwargs):
        httpretty.enable()

        fun(*args, **kwargs)

        httpretty.disable()
        httpretty.reset()

    return wrapper


class BBridgeClientTest(unittest.TestCase):
    content_type = "application/json"

    token = uuid.uuid4().hex
    host_url = "http://somin.io:1024/v1"

    client = BBridgeClient(token, host_url)

    @manage_httpretty
    def test_individual_user_profiling(self):
        expected_request_id = uuid.uuid4().hex
        expected_response = json.dumps({
            "profiling": {
                "gender": {
                    "label": "female",
                    "confidence": 0.5429273621882306
                }
            }})

        httpretty.register_uri(httpretty.POST, "{}/profiling/personal".format(self.host_url),
                               authorization=self.token,
                               body=json.dumps({"request_id": expected_request_id}), status=202)
        httpretty.register_uri(httpretty.GET, "{}/response".format(self.host_url), content_type=self.content_type,
                               authorization=self.token, body=expected_response, status=200)

        user = User(["cat is so cute!", "Scarlet is very good person"],
                    ["https://pbs.twimg.com/media/C279-WDXEAIg4lD.jpg"])
        request_id = self.client.individual_user_profiling(user, EN, [GENDER, AGE_GROUP]).body.request_id
        expect(request_id).to.equal(expected_request_id)

        response = self.client.response(request_id, UserProfile).body
        expect(response).to.an(UserProfile)
        response = self.client.response(request_id).body
        expect(response).to.an(dict)

    @manage_httpretty
    def test_image_objects_detection(self):
        expected_request_id = uuid.uuid4().hex
        expected_response = json.dumps(
            {"objects": [{"cls_name": "cat", "score": 0.86, "x": 200., "y": 340., "w": 190., "h": 310.}]})
        httpretty.register_uri(httpretty.POST, "{}/image/objects".format(self.host_url),
                               authorization=self.token,
                               body=json.dumps({"request_id": expected_request_id}), status=202)
        httpretty.register_uri(httpretty.GET, "{}/response".format(self.host_url), content_type=self.content_type,
                               authorization=self.token, body=expected_response, status=200)

        image = ObjectDetectionData("https://pbs.twimg.com/media/C279-WDXEAIg4lD.jpg", 0.7)
        request_id = self.client.image_objects_detection(image).body.request_id
        expect(request_id).to.equal(expected_request_id)

        response = self.client.response(request_id, ImageObjects).body
        expect(response).to.an(ImageObjects)
        response = self.client.response(request_id).body
        expect(response).to.an(dict)

    @manage_httpretty
    def test_image_concepts_detection(self):
        expected_request_id = uuid.uuid4().hex
        expected_response = json.dumps({"results": [{"concepts": {"lollipop": 0.013954441, "miniskirt": 0.07939269}}, {
            "error": "Error while downloading ttps://pbs.twimg.com/media/C279-WDXEAIg4lD.jpg"}]})

        httpretty.register_uri(httpretty.POST, "{}/image/concepts".format(self.host_url),
                               authorization=self.token,
                               body=json.dumps({"request_id": expected_request_id}), status=202)
        httpretty.register_uri(httpretty.GET, "{}/response".format(self.host_url), content_type=self.content_type,
                               authorization=self.token, body=expected_response, status=200)

        image = ConceptDetectionData(
            ["https://pbs.twimg.com/media/C279-WDXEAIg4lD.jpg", "ttps://pbs.twimg.com/media/C279-WDXEAIg4lD.jpg"], 5)
        request_id = self.client.image_concepts_detection(image).body.request_id
        expect(request_id).to.equal(expected_request_id)

        response = self.client.response(request_id, ImagesConcepts).body
        expect(response).to.an(ImagesConcepts)
        response = self.client.response(request_id).body
        expect(response).to.an(dict)

    @manage_httpretty
    def test_pos_tagging(self):
        expected_request_id = uuid.uuid4().hex
        expected_response = json.dumps({"results": [[{"text": "cat", "type": "NN"}]]})
        httpretty.register_uri(httpretty.POST, "{}/nlp/pos".format(self.host_url),
                               authorization=self.token,
                               body=json.dumps({"request_id": expected_request_id}), status=202)
        httpretty.register_uri(httpretty.GET, "{}/response".format(self.host_url), content_type=self.content_type,
                               authorization=self.token, body=expected_response, status=200)

        nlp_data = NLPData(["cat is so cute!"])
        request_id = self.client.pos_tagging(nlp_data, EN).body.request_id
        expect(request_id).to.equal(expected_request_id)

        response = self.client.response(request_id, POSTagging).body
        expect(response).to.an(POSTagging)
        response = self.client.response(request_id).body
        expect(response).to.an(dict)

    @manage_httpretty
    def test_sentiment_analysis(self):
        expected_request_id = uuid.uuid4().hex
        expected_response = json.dumps({"results": [0.7]})
        httpretty.register_uri(httpretty.POST, "{}/nlp/sentiment".format(self.host_url),
                               authorization=self.token,
                               body=json.dumps({"request_id": expected_request_id}), status=202)
        httpretty.register_uri(httpretty.GET, "{}/response".format(self.host_url), content_type=self.content_type,
                               authorization=self.token, body=expected_response, status=200)

        nlp_data = NLPData(["cat is so cute!"])
        request_id = self.client.sentiment_analysis(nlp_data, EN).body.request_id
        expect(request_id).to.equal(expected_request_id)

        response = self.client.response(request_id, Sentiments).body
        expect(response).to.an(Sentiments)
        response = self.client.response(request_id).body
        expect(response).to.an(dict)

    @manage_httpretty
    def test_named_entity_recognition(self):
        expected_request_id = uuid.uuid4().hex
        expected_response = json.dumps({"results": [[]]})
        httpretty.register_uri(httpretty.POST, "{}/nlp/ner".format(self.host_url),
                               authorization=self.token,
                               body=json.dumps({"request_id": expected_request_id}), status=202)
        httpretty.register_uri(httpretty.GET, "{}/response".format(self.host_url), content_type=self.content_type,
                               authorization=self.token, body=expected_response, status=200)

        nlp_data = NLPData(["cat is so cute!"])
        request_id = self.client.name_entity_recognition(nlp_data, EN).body.request_id
        expect(request_id).to.equal(expected_request_id)

        response = self.client.response(request_id, NER).body
        expect(response).to.an(NER)
        response = self.client.response(request_id).body
        expect(response).to.an(dict)

    @manage_httpretty
    def test_topics(self):
        expected_request_id = uuid.uuid4().hex
        expected_response = json.dumps({
            "topics_list": [
            {
              "topics": {
                "Gadgets": 0.07621672553053785,
                "Religion": 0.11730666259705776,
                "Business Insurance": 0.43024605909174013,
                "Greetings": 0.035481042999789277,
                "Emotions Positive": 0.030850648983692486
              }
            }]})

        httpretty.register_uri(httpretty.POST, "{}/topics/latent".format(self.host_url),
                               authorization=self.token,
                               body=json.dumps({"request_id": expected_request_id}), status=202)
        httpretty.register_uri(httpretty.GET, "{}/response".format(self.host_url), content_type=self.content_type,
                               authorization=self.token, body=expected_response, status=200)

        document_data = DocumentsData([["For the precise calculation of your report we may need an estimation of your age and location. \
        You can share your results with your friends but we will never share your answers or your facebook information."]], 5)
        request_id = self.client.topic_detection(document_data, EN, INSURANCE).body.request_id
        expect(request_id).to.equal(expected_request_id)

        response = self.client.response(request_id, TopicDistribution).body
        expect(response).to.an(TopicDistribution)
        response = self.client.response(request_id).body
        expect(response).to.an(dict)


if __name__ == '__main__':
    unittest.main()
