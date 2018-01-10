class UserID(object):
    def __init__(self, data_source, user_name):
        """
        :type __data_source: str
        :type __user_name: str
        """
        self.__data_source = data_source
        self.__user_name = user_name

    @property
    def data_source(self):
        return self.__data_source

    @property
    def user_name(self):
        return self.__user_name
