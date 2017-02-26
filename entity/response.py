import json
from httplib import OK


class Response(object):
    def __init__(self, body, status_code=OK, err_message=None):
        """
        :type body: str | entity.response.APIResponse | None
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


class APIResponse(object):
    def __init__(self, request_id, content):
        """
        :type request_id: str
        :type content: dict | object
        """
        self.__request_id = request_id
        self.__content = content

    @property
    def request_id(self):
        return self.__request_id

    @property
    def content(self):
        return self.__content

    @staticmethod
    def from_json(json_object, inner_type=None):
        """
        :type json_object: dict
        :type inner_type: type
        :rtype: entity.response.APIResponse
        """
        content = json_object["content"]
        if inner_type is not None:
            type_from_json = getattr(inner_type, "from_json")
            content = type_from_json(content)
        return APIResponse(json_object["requestId"], content)

    @staticmethod
    def from_json_str(json_string, inner_type=None):
        """
        :type json_string: str
        :type inner_type: type
        :rtype: entity.response.APIResponse
        """
        return APIResponse.from_json(json.loads(json_string), inner_type)
