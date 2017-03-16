class Response(object):
    def __init__(self, body, status_code=200, err_message=None):
        """
        :type body: entity.bbridge_entity.BBridgeEntity | dict | None
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
