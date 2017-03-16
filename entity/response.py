import json


class Response(object):
    def __init__(self, body, status_code=200, err_message=None):
        """
        :type body: object | None
        :type status_code: int
        :type err_message: str | None
        """
        self.__body = body
        self.__status_code = status_code
        self.__err_message = err_message

    @property
    def body(self):
        return self.__body

    @property
    def status_code(self):
        return self.__status_code

    @property
    def err_message(self):
        return self.__err_message


class RequestId(object):
    def __init__(self, request_id):
        """
        :type request_id: str
        """
        self.__request_id = request_id

    @property
    def request_id(self):
        return self.__request_id

    @staticmethod
    def from_json(json_object):
        """
        :type json_object: dict
        :rtype: entity.response.RequestId
        """
        return RequestId(json_object["request_id"])

    @staticmethod
    def from_json_str(json_string):
        """
        :type json_string: str
        :rtype: entity.response.RequestId
        """
        return RequestId.from_json(json.loads(json_string))
